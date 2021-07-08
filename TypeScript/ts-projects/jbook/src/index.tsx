import * as esbuild from 'esbuild-wasm';
import { useState, useEffect, useRef } from 'react';
import ReactDOM from 'react-dom';

const App = () => {
  const [input, setInput] = useState<string>('');
  const [code, setCode] = useState<string>('');
  const serviceRef = useRef<any>(null);
  const textRef = useRef<HTMLTextAreaElement | null>(null);

  useEffect(() => {
    startService()

    if (!textRef.current) {
      return;
    }

    textRef.current.focus();
  }, []);

  const startService = async () => {
    serviceRef.current = await esbuild.startService({
      worker: true,
      wasmURL: '/esbuild.wasm'
    });
    
  }

  const onClick = async () => {
    if (!serviceRef.current) {
      return;
    }
    const result = await serviceRef.current.transform(input, {
      loader: 'jsx',
      target: 'es2015'
    });

    setCode(result.code)
  };

  return (
    <div>
      <textarea
        ref={textRef}
        value={input}
        onChange={(e) => setInput(e.target.value)}
      ></textarea>
      <div>
        <button onClick={onClick}>Submit</button>
      </div>
      <pre>{code}</pre>
    </div>
  );
};

ReactDOM.render(<App />, document.querySelector('#root'));

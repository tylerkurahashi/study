import * as esbuild from 'esbuild-wasm';
import { useState, useEffect, useRef } from 'react';
import ReactDOM from 'react-dom';

import { unpkgPathPlugin } from './plugins/unpkg-path-plugin';
import { fetchPlugin } from './plugins/fetch-plugin';
import CodeEditor from './components/code-editor';

const App = () => {
  const [input, setInput] = useState<string>('');
  const iframe = useRef<any>();
  const serviceRef = useRef<any>();
  const textRef = useRef<HTMLTextAreaElement | null>(null);

  useEffect(() => {
    startService();

    console.log(textRef);

    if (!textRef.current) {
      return;
    }

    textRef.current.focus();
  }, []);

  const startService = async () => {
    serviceRef.current = await esbuild.startService({
      worker: true,
      wasmURL: 'https://unpkg.com/esbuild-wasm@0.8.27/esbuild.wasm',
    });
  };

  const onClick = async () => {
    if (!serviceRef.current) {
      return;
    }

    iframe.current.srcdoc = html;

    const result = await serviceRef.current.build({
      entryPoints: ['index.js'],
      bundle: true,
      write: false,
      plugins: [unpkgPathPlugin(), fetchPlugin(input)],
      define: {
        'process.env.NODE_ENV': '"production"',
        global: 'window',
      },
    });

    console.log(result);

    // setCode(result.outputFiles[0].text);
    iframe.current.contentWindow.postMessage(result.outputFiles[0].text, '*')
  };

  const html = `
    <html>
      <head></head>
      <body>
        <div id="root"></div>
        <script>
          window.addEventListener('message', (event) => {
            try {
              eval(event.data)
            } catch (err) {
              const root = document.querySelector('#root');
              root.innerHTML = '<div style="color: red;"><h4>Runtime Error</h4>' + err + '</div>'
            }
          }, false);
        </script>
      </body>
    </html>
  `

  return (
    <div>
      <CodeEditor initialValue={input} onChange={(value)=> setInput(value)} />
      <textarea
        ref={textRef}
        value={input}
        onChange={(e) => setInput(e.target.value)}
      ></textarea>
      <div>
        <button onClick={onClick}>Submit</button>
      </div>
      <iframe title='code-review' ref={iframe} sandbox='allow-scripts' srcDoc={html}/>
    </div>
  );
};

ReactDOM.render(<App />, document.querySelector('#root'));

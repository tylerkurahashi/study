import { useState } from 'react';
import ReactDOM from 'react-dom';

import CodeEditor from './components/code-editor';
import Preview from './components/previews';
import bundle from './bundler';

const App = () => {
  const [input, setInput] = useState<string>('');
  const [code, setCode] = useState<string>('');

  const onClick = async () => {
    const output = await bundle(input)
    setCode(output);
  };

  return (
    <div>
      <CodeEditor initialValue={input} onChange={(value)=> setInput(value)} />
      <div>
        <button onClick={onClick}>Submit</button>
      </div>
      <Preview code={code}/>
    </div>
  );
};

ReactDOM.render(<App />, document.querySelector('#root'));

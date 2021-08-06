import { useState } from 'react';

import CodeEditor from './code-editor';
import Preview from './previews';
import bundle from '../bundler';
import Resizable from './resizable';

const CodeCell = () => {
  const [input, setInput] = useState<string>('');
  const [code, setCode] = useState<string>('');

  const onClick = async () => {
    const output = await bundle(input);
    setCode(output);
  };

  return (
    <Resizable direction="vertical">
      <div>
        <CodeEditor
          initialValue={input}
          onChange={(value) => setInput(value)}
        />
        <div>
          <button onClick={onClick}>Submit</button>
        </div>
        <Preview code={code} />
      </div>
    </Resizable>
  );
};

export default CodeCell;
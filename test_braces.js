const fs = require('fs');

const code = fs.readFileSync('test.js', 'utf8');

let stack = [];
for (let i = 0; i < code.length; i++) {
  if (code[i] === '{') {
    stack.push(i);
  } else if (code[i] === '}') {
    if (stack.length === 0) {
      // Ignored for now
    } else {
      stack.pop();
    }
  }
}

if (stack.length > 0) {
  let idx = stack[stack.length - 1];
  console.log('Unmatched { at index', idx);
  console.log('Context:\n', code.substring(Math.max(0, idx - 100), Math.min(code.length, idx + 100)));
}

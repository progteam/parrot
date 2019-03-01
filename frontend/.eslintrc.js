module.exports = {
  env: {
    browser: true,
    es6: true,
  },
  extends: 'airbnb',
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: [
    'react',
  ],
  rules: {
    // We use webpack so not all dependencies are listed in package.json
    "import/no-extraneous-dependencies": [0],
    // We allow mix jsx with js code
    "react/jsx-filename-extension": [1, { "extensions": [".js", ".jsx"] }],
  },
};

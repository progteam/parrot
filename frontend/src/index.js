import React from 'react';
import ReactDOM from 'react-dom';

import LandingPage from './landing/landing';

import './index.scss';

const App = () => (
  <div>
    <LandingPage />
  </div>
);

ReactDOM.render(<App />, document.getElementById('root'));

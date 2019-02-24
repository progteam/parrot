import React from 'react';
import ReactDOM from 'react-dom';

import LandingPage from './landing/landing'

import './index.scss';

class App extends React.Component {
  render() {
    return (
      <div>
        <LandingPage />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));

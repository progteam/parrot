import React from 'react';
import ReactDOM from 'react-dom';

import './index.scss';
import LandingPage from './landing/landing'

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

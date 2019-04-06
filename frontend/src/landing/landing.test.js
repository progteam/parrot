import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import LandingPage from './landing';

/*
 * it comes with Jtest, so we disable the no-undef error.
 */

/* eslint-disable no-undef */
it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(
    <Router>
      <LandingPage />
    </Router>,
    div,
  );
  ReactDOM.unmountComponentAtNode(div);
});

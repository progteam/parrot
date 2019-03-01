import React from 'react';
import ReactDOM from 'react-dom';
import LandingPage from './landing';

/*
 * it comes with Jtest, so we disable the no-undef error.
 */

/* eslint-disable no-undef */
it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<LandingPage />, div);
  ReactDOM.unmountComponentAtNode(div);
});

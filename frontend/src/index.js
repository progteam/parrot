import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';

import AboutPage from './about/about';
import EventsPage from './events/events';
import LandingPage from './landing/landing';
import Page404 from './page404/page404';

import './index.scss';

const App = () => (
  <Router>
    <div>
      <Switch>
        <Route exact path="/" component={LandingPage} />
        <Route exact path="/about" component={AboutPage} />
        <Route exact path="/events" component={EventsPage} />
        <Route component={Page404} />
      </Switch>
    </div>
  </Router>
);

ReactDOM.render(<App />, document.getElementById('root'));

import React from 'react';

import UserDelta from './user_delta';

import './scoreboard_delta.scss';

class ScoreBoardDelta extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      users: [
        {
          name: 'Donald',
          handle: 'javiercaudillo10',
          delta: 10,
        },
        {
          name: 'Fernando',
          handle: 'javiercaudillo10',
          delta: -1,
        },
        {
          name: 'Miorel',
          handle: 'javiercaudillo10',
          delta: 5,
        },
        {
          name: 'Emma',
          handle: 'javiercaudillo10',
          delta: 2,
        },
      ],
    };
  }

  render() {
    const {
      users,
    } = this.state;

    // get max Delta of all users
    const maxDelta = users.reduce((a, b) => (a.delta > b.delta ? a : b)).delta;

    // convert any negatives to '0'
    const usersZeroDelta = users.map((obj) => {
      const temp = obj;
      temp.delta = (obj.delta > 0 ? obj.delta : 0);
      return temp;
    });

    // sort props to promote being a top performer
    usersZeroDelta.sort((a, b) => b.delta - a.delta);

    // populate a list of UserDelta with props
    const userInfo = usersZeroDelta.map(obj => <UserDelta {...obj} maxDelta={maxDelta} />);

    return (
      <div className="scoreboard_delta">
        <h2> User Delta for Today </h2>
        {userInfo}
      </div>
    );
  }
}

export default ScoreBoardDelta;

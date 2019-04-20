import React from 'react';
import axios from 'axios';

import UserDelta from './user_delta';

import './scoreboard_delta.scss';

class ScoreboardDelta extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      users: [],
      timeFrames: ['day', 'week', 'month'],
      timeFrameIndex: 1,
    };

    this.getUserData = this.getUserData.bind(this);
  }

  componentDidMount() {
    this.getUserData(1);
  }

  async getUserData(timeFrameIndex) {
    const {
      timeFrames,
    } = this.state;
    const res = await axios.get(`/scoreboard/${timeFrames[timeFrameIndex]}`);
    const { data } = res;
    this.setState({
      users: data,
      timeFrameIndex,
    });
  }

  render() {
    const {
      users,
      timeFrameIndex: tfi,
    } = this.state;

    // get max Delta of all users
    const maxDelta = users.reduce((a, b) => (a.points > b.points ? a : b), 0).points;

    // sort props to promote being a top performer
    users.sort((a, b) => b.points - a.points);

    // populate a list of UserDelta with props
    const userInfo = users.map(
      obj => <UserDelta {...obj} key={obj.username} maxDelta={maxDelta} />,
    );

    const textTimeFrame = () => {
      if (tfi === 0) return ' Today';
      if (tfi === 1) return ' this Week';
      return ' this Month';
    };

    return (
      <div className="scoreboard-delta">
        <div className="scoreboard-delta-top-bar">
          <h2>
            User Delta for
            {textTimeFrame()}
          </h2>
          <div>
            <button type="button" className="timeframe day" onClick={() => this.getUserData(0)}>Day</button>
            <button type="button" className="timeframe week" onClick={() => this.getUserData(1)}>Week</button>
            <button type="button" className="timeframe month" onClick={() => this.getUserData(2)}>Month</button>
          </div>
        </div>
        {userInfo}
      </div>
    );
  }
}

export default ScoreboardDelta;

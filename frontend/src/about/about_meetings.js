import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import './about_meetings.scss';

const Meeting = ({
  dayOfWeek,
  room,
  timeEnd,
  timeStart,
}) => (
  <div className="meeting">
    <div className="day-of-week">{dayOfWeek}</div>
    <div className="time-start">{timeStart}</div>
    <div className="to">-</div>
    <div className="time-end">{timeEnd}</div>
    <div className="room">{room}</div>
  </div>
);

Meeting.propTypes = {
  dayOfWeek: PropTypes.string.isRequired,
  room: PropTypes.string.isRequired,
  timeEnd: PropTypes.string.isRequired,
  timeStart: PropTypes.string.isRequired,
};

class Meetings extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      meetings: [],
    };
  }

  componentDidMount() {
    this.getMeetings();
  }

  async getMeetings() {
    const res = await axios.get('/about/meeting-info');
    const { data } = res;
    this.setState({
      meetings: data,
    });
  }

  render() {
    const { meetings } = this.state;
    // Avoid destructuring assignment here since we want to spread the args
    /* eslint-disable react/destructuring-assignment */
    return (
      <div className="meetings">
        <h3>Meeting Schedule S19</h3>
        {meetings.map(meeting => (
          <Meeting
            key={meeting.dayOfWeek}
            {...meeting}
          />
        ))}
      </div>
    );
  }
}

export default Meetings;

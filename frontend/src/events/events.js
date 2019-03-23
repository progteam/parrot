import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import GuestNav from '../components/guest_nav';
import Teams from './teams';

import './events.scss';

const Event = ({
  date,
  desc,
  div1Scoreboard,
  div2Scoreboard,
  imgUrl,
  name,
  teams,
}) => {
  /*
   * Filter the teams by division
   */
  const div1Teams = [];
  const div2Teams = [];
  teams.forEach((team) => {
    const { division } = team;
    switch (division) {
      case '1':
        div1Teams.push(team);
        break;
      case '2':
        div2Teams.push(team);
        break;
      default:
        break;
    }
  });
  const div1TeamsSection = div1Teams.length ? (
    <Teams
      scoreboard={div1Scoreboard}
      teams={div1Teams}
      division="Division 1"
    />
  ) : null;
  const div2TeamsSection = div2Teams.length ? (
    <Teams
      scoreboard={div2Scoreboard}
      teams={div2Teams}
      division="Division 2"
    />
  ) : null;
  /*
   * The admins should have the privilege to update the content of this
   * component, as HTML. Thus, we disable the lint warning here.
   */

  /* eslint-disable react/no-danger */
  return (
    <div className="event">
      <div className="left-panel">
        <img src={imgUrl} alt={name} />
        <div className="title">{name}</div>
        <div className="date">{date}</div>
      </div>
      <div className="right-panel">
        {div1TeamsSection}
        {div2TeamsSection}
        <div className="desc" dangerouslySetInnerHTML={{ __html: desc }} />
      </div>
    </div>
  );
};

Event.propTypes = {
  date: PropTypes.string.isRequired,
  desc: PropTypes.string,
  div1Scoreboard: PropTypes.string,
  div2Scoreboard: PropTypes.string,
  imgUrl: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  teams: PropTypes.arrayOf(PropTypes.object),
};

Event.defaultProps = {
  desc: null,
  div1Scoreboard: null,
  div2Scoreboard: null,
  teams: [],
};

class EventsPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      events: [],
    };
  }

  componentDidMount() {
    this.getEvents();
  }

  async getEvents() {
    const res = await axios.get('/events/data');
    const { data } = res;
    this.setState({
      events: data,
    });
  }

  render() {
    const { events } = this.state;
    return (
      <div className="events-page">
        <GuestNav />
        <div className="events">
          {events.map(e => (
            <Event key={e.name} {...e} />
          ))}
        </div>
      </div>
    );
  }
}

export default EventsPage;

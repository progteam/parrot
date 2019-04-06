import React from 'react';
import PropTypes from 'prop-types';

import './teams.scss';

const Team = ({
  members,
  name,
  rank,
}) => (
  <div className="team">
    <div className="team-name">
      <div className="team-rank">{rank}</div>
      {name}
    </div>
    <div className="members">
      {members.map(m => (
        <a
          key={m.name}
          href={m.profileUrl}
          rel="noopener noreferrer"
          target="_blank"
          className="member"
        >
          {m.name}
        </a>
      ))}
    </div>
  </div>
);

Team.propTypes = {
  members: PropTypes.arrayOf(PropTypes.shape({
    name: PropTypes.string.isRequired,
    profileUrl: PropTypes.string,
  })).isRequired,
  name: PropTypes.string.isRequired,
  rank: PropTypes.number.isRequired,
};

const Teams = ({
  division,
  scoreboard,
  teams,
}) => (
  <div>
    <div className="teams">
      <div className="division">
        {division}
        <div className="scoreboard">
          <a
            href={scoreboard}
            rel="noopener noreferrer"
            target="_blank"
          >
            scoreboard
          </a>
        </div>
      </div>
      {teams.map(team => (
        <Team key={team.rank} {...team} />
      ))}
    </div>
  </div>
);

Teams.propTypes = {
  division: PropTypes.string.isRequired,
  scoreboard: PropTypes.string,
  teams: PropTypes.arrayOf(PropTypes.shape(Team.propTypes)).isRequired,
};

Teams.defaultProps = {
  scoreboard: null,
};

export default Teams;

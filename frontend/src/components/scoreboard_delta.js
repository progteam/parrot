import React from 'react';

import UserDelta from './user_delta';

import './scoreboard_delta.scss';

class ScoreBoardDelta extends React.Component{
	constructor(props){
		super(props);

		this.state = {
			"users" : [
				{
					"name" : "Fernando Caudillo",
					"handle" : "javiercaudillo10",
					"delta" : 10
				},
				{
					"name" : "Fernando Caudillo",
					"handle" : "javiercaudillo10",
					"delta" : -1
				},
				{
					"name" : "Fernando Caudillo",
					"handle" : "javiercaudillo10",
					"delta" : 5
				},
				{
					"name" : "Fernando Caudillo",
					"handle" : "javiercaudillo10",
					"delta" : 2
				},
				
			]
		};
	}

	render(){
		// get max Delta of all users
		let maxDelta = 0;
		for(let user of this.state.users){
			maxDelta = Math.max(maxDelta, user.delta);
		}

		// convert any negatives to '0'
		this.state.users.map( (user) => {user.delta = (user.delta < 0 ? 0 : user.delta)} );

		// sort props to promote being a top performer
		this.state.users.sort( (a,b) => b.delta - a.delta);
		
		// populate a list of UserDelta with props
		const userInfo = this.state.users.map( (obj) => <UserDelta {...obj} maxDelta={maxDelta}/> );

		return(
			<div className="scoreboard_delta">
				<h2> User Delta for Today </h2>
				{userInfo}
			</div>
		);
	}
}

export default ScoreBoardDelta;

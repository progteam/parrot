import React from 'react';

import './user_delta.scss';

class UserDelta extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		const percentWidth = this.props.delta / this.props.maxDelta;
		const onDemandResize = {
			width: 100*percentWidth + "%"
		};
		console.log(this.props.delta + " " + this.props.maxDelta + " " + percentWidth);
		return(
			<div className='user_bar'>
				<div className='user_name'>
					<strong> {this.props.name} </strong>
				</div>
				<div className={'user_delta'+ (percentWidth === 0 ? 'zero_delta':'')} style={onDemandResize} > 
					{this.props.delta}
				</div>
			</div>
		);
	}

}

export default UserDelta;

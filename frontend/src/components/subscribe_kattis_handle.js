import React from 'react';

import './subscribe_kattis_handle.scss';

class SubKatHandle extends React.Component{
	constructor(props){
		super(props);

		this.state = {
			kattisHandle: '',
		};

		this.submitKattisHandle = this.submitKattisHandle.bind(this);
		this.handleChange = this.handleChange.bind(this);
	}
	handleChange(event){
		this.setState({kattisHandle: event.target.value});
	}
	submitKattisHandle(event){
		console.log(this.state.kattisHandle);
	}
	render(){
		return(
			<div className="form">

				<label htmlFor="kattisHandleBox">
					<strong> Subscribe to the graph! </strong>
				</label>
				
				<input name="kattisHandleBox" type="text" value={this.state.kattisHandle} placeholder=" Kattis Handle" onChange={this.handleChange}/>

				<button type="button" onClick={this.submitKattisHandle}>Subscribe</button>
			</div>
		);
	};

}

export default SubKatHandle;

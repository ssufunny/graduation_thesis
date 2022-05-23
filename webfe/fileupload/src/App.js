import React, { Component } from 'react';
import './App.css';
import baseimg from './upload.png';
export class App extends Component {
  state={
    profileImg: null
  }
  imageHandler = (e) => {
    const reader = new FileReader();
    reader.onload = () =>{
      if(reader.readyState === 2){
        this.setState({profileImg: reader.result})
      }
    }
    reader.readAsDataURL(e.target.files[0])
  };
	render() {
    const { profileImg} = this.state
		return (
			<div className="page">
				<div className="container">
					<h1 className="heading">Add your Image</h1>
					<div className="img-holder">
						<img src={profileImg} alt="" id="img" className="img" />
					</div>
            <input type="file" accept="image/*" name="image-upload" id="input" onChange={this.imageHandler}/>
					<div className="label">
          <label className="image-upload" htmlFor="input">
						업로드
					</label>
          <label className="image-upload" htmlFor="input">
						위치 찾기
					</label>
          </div>
				</div>
			</div>
		);
	}
}

export default App;


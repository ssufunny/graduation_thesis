import React from "react";
import './styles.css';
import './index.css';

class Main extends React.Component{
    constructor(props){
        super(props);
        this.state={
            files : []
        };
        this.onChange = this.onChange.bind(this);
    }
    onChange(e){
        var files = e.target.files;
        // slice: 얕은복사 (원본데이터 보존한채 복사, 훼손 안되는 장점)
        // call : 상위의 context를 변경한느 메서드 "변경"
        var filesArr = Array.prototype.slice.call(files);
        // ... : 전개연산자 : 정해지지 않은 갯수의 매개변수
        this.setState({files: [...this.state.files, ...filesArr]})
    }

    removeFile(f){
        this.setState({files:this.state.files.filter(x => x!==f)})
    }

    // 22번째줄에서 onchange일어나면 9번째줄에 있는거 실행해주는,,?
    render(){
        return(
            <form>
                <div>
                    <label className="custom-file-upload">
                        <input type="file" multiple onChange={this.onChange}/> 
                        파일 올리기
                    </label>
                    {
                        this.state.files.map(x=> <div className="file-preview" onClick={this.removeFile.bind(this,x)}>{x.name}</div>)
                    }
                </div>
                <div className="wrap">
                    <a href="#" className="button">전송</a>
                </div>
            </form>
        )
    };
}
export default Main;
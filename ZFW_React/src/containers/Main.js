import React, { Component } from 'react';
import { Nav , Navbar } from 'react-bootstrap';

import Home from './Home';

// import components
import SchInfo from './school/Info';
// import SchScore4 from './school/Score4';
// import T from '../components/ClassGrade1';
import SchConsumption from './school/Consumption';
// import ClassCsp from '../components/ClassCsp'
// import SchoolConsumption from '../components/SchoolConsumption';

import SchAttend from './school/Attendance'
import ChooseSub from './application/3In7'
import StudentInfo from './student/Student.js'

import 'bootstrap/dist/css/bootstrap.min.css';
import '../css/main.css';

class Main extends Component {
    constructor(props) {
        super(props);
        this.state = {
            whichShow: 'home',
            menuShow: true,
            switchButtonState: false,
        };
        this.menu = [{
            header: "学校层面",
            body: ["基本信息统计", "师资分配情况", "成绩统计分析", "考勤信息统计", "消费信息分析"],
            content: [<SchInfo/>, , ,<SchAttend/>,<SchConsumption/>]
        }, {
            header: "班级层面",
            body: ["班级画像"],
            content: []
        }, {
            header: "学生层面",
            body: ["学生画像"],
            content: [<StudentInfo/>]
        }, {
            header: "应用层面",
            body: ["学生7选3推荐"],
            content: [<ChooseSub />]
        }];
        this.animation = {
            slideLeft: {animation: 'slideLeft 320ms ease 0s 1 normal forwards running'},
            slideRight: {animation: 'slideRight 320ms ease 0s 1 normal forwards running'},
        };
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick(idx) {
        if (idx !== 'home') {  // 返回首页不需要隐藏菜单栏
            const menuShow = !this.state.menuShow;
            const switchButtonState = !this.state.switchButtonState;
            this.setState({
                menuShow: menuShow,
                switchButtonState: switchButtonState,
            });
        }
        if (typeof idx === 'string') {  // 区分是点击菜单栏还是点击的按钮
            this.setState({whichShow: idx});
        }
    }
    getContent() {
        if (this.state.whichShow === 'home') {  // 渲染首页
            return <Home/>;
        }
        // 如果不是首页则根据索引渲染
        const numbers = this.state.whichShow.split('-');
        const n1 = parseInt(numbers[0]);
        const n2 = parseInt(numbers[1]);
        const temp = this.menu[n1].content[n2];
        return (
            <React.Fragment>
                <Head pretitle={this.menu[n1].header} title={this.menu[n1].body[n2]}/>
                {temp===undefined?<div>索引错误</div>:temp}
            </React.Fragment>
        );
    }
    render() {
        return (
            <React.Fragment>
                <div className="wrapper">
                    <SwitchButton state={this.state.switchButtonState} click={this.handleClick} animation={this.animation}/>
                    <MenuBar menu={this.menu} default={this.state.whichShow} click={this.handleClick} show={this.state.menuShow}/>
                    <div className='main'>
                        <div className='content' style={((this.state.menuShow)&(this.state.whichShow==='home'))?this.animation.slideRight:this.animation.slideLeft}>
                            {this.getContent()}
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

function MenuBar(props) {
    const slideLeftShow = {animation: 'slideLeft-show 320ms ease 0s 1 normal forwards running'};
    const slideRightHide = {animation: 'slideRight-hide 320ms ease 0s 1 normal forwards running'};
    return (
        <Navbar style={props.show?slideRightHide:slideLeftShow}>
            <div className="brand">
                <a href='javascript: void(0);' onClick={()=>{
                    props.click('home');
                }}>数智教育</a>
            </div>
            <Nav as="ul" className="flex-column menu" onSelect={k => props.click(k)}>
                {
                    props.menu.map((items, index)=>{
                        return <SingleNav key={index} idx={index} header={items.header} body={items.body} />
                    })
                }
            </Nav>
        </Navbar>
    );
}

function SingleNav(props) {
    return (
        <React.Fragment>
            <span>{props.header}</span>
            {
                props.body.map((items, index)=>{
                    return (
                        <Nav.Item as="li" key={index} className="menu-body">
                            <Nav.Link eventKey={props.idx + '-' + index}>{items}</Nav.Link>
                        </Nav.Item>
                    );
                })
            }
        </React.Fragment>
    );
}

function SwitchButton(props) {
    const rightArrow = <svg width="16px" height="16px" viewBox="0 0 1024 1024" ><path d="M245.034251 895.239428l383.063419-383.063419L240.001631 124.07997l0.070608-0.033769c-12.709463-13.137205-20.530592-31.024597-20.530592-50.731428 0-40.376593 32.736589-73.111135 73.115228-73.111135 19.705807 0 37.591153 7.819083 50.730405 20.528546l0.034792-0.035816 438.686251 438.681134-0.035816 0.034792c13.779841 13.281491 22.3838 31.915897 22.3838 52.586682 0 0.071631 0 0.106424 0 0.178055 0 0.072655 0 0.10847 0 0.144286 0 20.669762-8.603959 39.341007-22.3838 52.623521l0.035816 0.033769L343.426165 1003.661789l-0.180102-0.179079c-13.140275 12.565177-30.950919 20.313651-50.588165 20.313651-40.378639 0-73.115228-32.736589-73.115228-73.114205C219.544717 928.512229 229.432924 908.664182 245.034251 895.239428z" fill="#ffffff" /></svg>
    const leftArrow = <svg width="16px" height="16px" viewBox="0 0 1024 1024" ><path d="M778.965749 128.759549l-383.064442 383.063419 388.097062 388.096039-0.070608 0.033769c12.709463 13.137205 20.529569 31.024597 20.529569 50.731428 0 40.376593-32.736589 73.112158-73.115228 73.112158-19.705807 0-37.591153-7.819083-50.730405-20.528546l-0.034792 0.035816L241.890654 564.622498l0.035816-0.035816c-13.779841-13.281491-22.3838-31.915897-22.3838-52.585659 0-0.071631 0-0.106424 0-0.178055 0-0.072655 0-0.10847 0-0.144286 0-20.669762 8.603959-39.341007 22.3838-52.622498l-0.035816-0.034792L680.573835 20.337187l0.180102 0.179079c13.139252-12.5662 30.950919-20.313651 50.587142-20.313651 40.378639 0 73.115228 32.736589 73.115228 73.114205C804.455283 95.485725 794.567076 115.334795 778.965749 128.759549z" fill="#ffffff" /></svg>
    const arrow = props.state?rightArrow:leftArrow;
    const animation = props.state?props.animation.slideLeft:props.animation.slideRight;
    return (
        <button className='switch-button' style={animation} onClick={props.click}>{arrow}</button>
    );
}

function Head(props) {
    return (
        <div className='header-body'>
            <div className='row'>
                <div className='col'>
                    <h6 className='header-pretitle'>{props.pretitle}</h6>
                    <h1 className='header-title'>{props.title}</h1>
                </div>
            </div>
        </div>
    );
}

export default Main;

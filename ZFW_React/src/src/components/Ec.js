import React, { Component } from 'react';
import * as echarts from 'echarts';

export default class extends Component {
    static defaultProps = {
        option: {},
        w: undefined,
        h: undefined,
        per: 1,
        setOption: false,
        resetOption: false,
    };
    constructor(props) {
        super(props);
        this.ecIns = null;
        this.ecDom = React.createRef();
    }
    componentWillReceiveProps(nextProps) {
        if (this.props.setOption) {
            this.ecIns.setOption(nextProps.option);
        }
        if (this.props.resetOption) {
            if (this.ecIns) {
                this.ecIns.clear();
                this.ecIns.dispose();
                this.ecIns = null;
            }
            const dom = this.ecDom.current;
            this.ecIns = echarts.init(dom);
            this.ecIns.setOption(nextProps.option);
        }
    }
    componentDidMount() {
        const dom = this.ecDom.current;
        if (this.props.w) {
            dom.style.width = this.props.w;
        }
        if (this.props.h) {
            dom.style.height = this.props.h;
        }
        if (dom.clientHeight === 0) {
            dom.style.height = (dom.clientWidth * this.props.per) + 'px';
        }
        if (dom.clientWidth === 0) {
            dom.style.width = (dom.clientHeight / this.props.per) + 'px';
        }
        this.ecIns = echarts.init(dom);
        this.ecIns.setOption(this.props.option);
        setTimeout(()=>{
            if (this.ecIns) {
                this.ecIns.resize({
                    width: dom.clientWidth,
                    height: dom.clientHeight
                });
            }
        }, 1000)
    }
    componentWillUnmount() {
        if (this.ecIns) {
            this.ecIns.clear();
            this.ecIns.dispose();
            this.ecIns = null;
        }
    }
    render() {
        return (
            <div ref={this.ecDom}>
            </div>
        );
    }
}

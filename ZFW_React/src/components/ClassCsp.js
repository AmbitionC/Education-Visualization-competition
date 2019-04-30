import React from 'react';
import Ec from './Ec';
import cspJson from '../data/consumption/class_csp.json';

export default class extends React.Component {
    constructor(props) {
        super(props);
        this.date = [];
        this.total = [];
        this.peoNum = [];
        this.max = [];  // 这个max存放的值是max-min的值，即最大值与最小值的差值
        this.min = [];
        this.mean = [];
    }
    setData(oriJson) {
        this.date = oriJson.index;
        const oriData = oriJson.data;
        for (let i = 0; i< oriData.length; i ++) {
            const singleData = oriData[i];
            this.total.push(parseFloat(singleData[0].toFixed(2)));
            this.peoNum.push(parseInt(singleData[1]))
            this.max.push(parseFloat((singleData[2]-singleData[3]).toFixed(2)));
            this.min.push(parseFloat(singleData[3].toFixed(2)));
            this.mean.push(parseFloat(singleData[4].toFixed(2)));
        }
        return 0;
    }
    getOption1() {
        return {
            xAxis: {
                type : 'category',
                data : this.date
            },
            yAxis: {
                type : 'value'
            },
            series: [
                {
                    type: 'bar',
                    stack:  '最值',
                    itemStyle: {
                        normal: {
                            barBorderColor: 'rgba(0,0,0,0)',
                            color: 'rgba(0,0,0,0)'
                        },
                        emphasis: {
                            barBorderColor: 'rgba(0,0,0,0)',
                            color: 'rgba(0,0,0,0)'
                        }
                    },
                    data: this.min
                },
                {
                    type: 'bar',
                    stack: '最值',
                    data: this.max
                },
                {
                    type: 'line',
                    data: this.mean
                }
            ]
        };
    }
    getOption2() {
        return {
            xAxis: {
                data: this.date,
                silent: false,
                splitLine: {
                    show: false
                }
            },
            yAxis: [{

            }, {

            }],
            series: [{
                name: '消费总额',
                type: 'bar',
                data: this.total,
                animationDelay: function (idx) {
                    return idx * 2;
                }
            }, {
                name: '消费人数',
                type: 'bar',
                yAxisIndex: 1,
                data: this.peoNum,
                animationDelay: function (idx) {
                    return idx * 2 + 100;
                }
            }],
        };
    }
    componentWillMount() {
        this.setData(cspJson);
    }
    render() {
        return (
            <div>
                <Ec option={this.getOption1()} h='400px' />
                <Ec option={this.getOption2()} h='400px' />
            </div>
        );
    }
}

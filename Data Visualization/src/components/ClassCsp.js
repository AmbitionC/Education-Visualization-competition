import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import cspJson from '../data/consumption/class/class920_csp.json';

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
            color: ['#749aa0', '#df6b66'],
            title: {
                text: '日消费最值、均值',
                left: 'center',
                textStyle: {
                    fontWeight: 400,
                    fontSize: 15,
                }
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross'
                },
                formatter: (params) => {
                    let res = [];
                    for (let i = 0; i < params.length; i ++) {
                        res.push(params[i].data);
                    }
                    return params[0].name + '<br/>最低消费: ' + res[0].toFixed(2) + '<br/>最高消费: ' + (res[0] + res[1]).toFixed(2) + '<br/>平均消费: ' + res[2].toFixed(2);
                }
            },
            grid: {
                left: 0,
                right: 0,
                top: '15%',
                bottom: '12%',
                containLabel: true
            },
            xAxis: {
                type : 'category',
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                data : this.date
            },
            yAxis: {
                type : 'value',
                axisLabel: {
                    formatter: '{value}元'
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                }
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
                    showSymbol: false,
                    data: this.mean
                }
            ]
        };
    }
    getOption2() {
        return {
            color: ['#f59f48', '#8cc1aa'],
            title: {
                text: '日消费总值',
                left: 'center',
                textStyle: {
                    fontWeight: 400,
                    fontSize: 15,
                }
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross'
                }
            },
            legend: {
                bottom: 'bottom',
            },
            grid: {
                left: 0,
                right: 0,
                top: '15%',
                bottom: '12%',
                containLabel: true
            },
            xAxis: {
                data: this.date,
                silent: false,
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }
            },
            yAxis: [{
                type : 'value',
                axisLabel: {
                    formatter: '{value}元'
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                }
            }, {
                type : 'value',
                axisLabel: {
                    formatter: '{value}人'
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                }
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
            <Card>
                <Card.Header>
                    <h4>2-6 消费情况</h4>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.getOption1()} h='240px' />
                    <Ec option={this.getOption2()} h='240px' />
                </Card.Body>
            </Card>
        );
    }
}

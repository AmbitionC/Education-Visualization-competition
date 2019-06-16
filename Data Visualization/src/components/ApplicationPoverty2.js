import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';

import povertyHelper3 from '../data/povertyHelper/PovertyHelper3.json'
import povertyHelper4 from '../data/povertyHelper/PovertyHelper4.json'

const date = povertyHelper3.date;
const poverty_studentID = povertyHelper3.studentID
const normal_studentID = povertyHelper4.studentID 

export default function() {
    const option = {
        title: [{
            text: "贫困生日常消费",
            left: '18%',
            textStyle: {
                fontWeight: 500,
                fontSize: 15,
            }
        },{
            text: "非贫困生日常消费",
            right: '19%',
            textStyle: {
                fontWeight: 500,
                fontSize: 15,
            }
        }],
        legend: {
            left: 'center',
            bottom: 'bottom',
            selectedMode: 'single'
        },
        tooltip: {
            formatter: function(params) {
                return [
                    '学生ID：' + params.data[0],
                    '消费日期：' + params.data[1] + '号',
                    '消费总金额：' + parseInt(params.data[2]) + '元'
                    ].join('<br/>')
            }
        },
        grid: [{
            left: 0,
            right: '56%',
            top: '12%',
            bottom: '10%',
            containLabel: true
        },{
            left: '51%',
            right: '5%',
            top: '12%',
            bottom: '10%',
            containLabel: true
        }],
        xAxis: [{
            name: '学生ID',
            nameGap: 10,
            type: 'category',
            splitLine: {show: false},
            axisTick: {show: false},
            axisLabel: {show: false},
            data: poverty_studentID,
            gridIndex: 0
        },{
            name: '学生ID',
            nameGap: 10,
            type: 'category',
            splitLine: {show: false},
            axisTick: {show: false},
            axisLabel: {show: false},
            data: normal_studentID,
            gridIndex: 1
        }],
        yAxis: [{
            name: '日期',
            nameGap: 10,
            type: 'category',
            splitLine: {show: false},
            axisTick: {show: false},
            data: date,
            gridIndex: 0
        },{
            name: '日期',
            nameGap: 10,
            type: 'category',
            splitLine: {show: false},
            axisTick: {show: false},
            data: date,
            gridIndex: 1
        }],
        series: [
            {
                name: '2018/09',
                xAxisIndex: 0,
                yAxisIndex: 0,
                type: 'scatter',
                data: povertyHelper3.dec,
                itemStyle: {
                    color: '#df6b66'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },{
                name: '2018/10',
                xAxisIndex: 0,
                yAxisIndex: 0,
                type: 'scatter',
                data: povertyHelper3.oct,
                itemStyle: {
                    color: '#df6b66'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },{
                name: '2018/11',
                xAxisIndex: 0,
                yAxisIndex: 0,
                type: 'scatter',
                data: povertyHelper3.nov,
                itemStyle: {
                    color: '#df6b66'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            }, {
                name: '2018/12',
                xAxisIndex: 0,
                yAxisIndex: 0,
                type: 'scatter',
                data: povertyHelper3.sept,
                itemStyle: {
                    color: '#df6b66'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },{
                name: '2019/01',
                xAxisIndex: 0,
                yAxisIndex: 0,
                type: 'scatter',
                data: povertyHelper3.jan,
                itemStyle: {
                    color: '#df6b66'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },{
                name: '2018/09',
                xAxisIndex: 1,
                yAxisIndex: 1,
                type: 'scatter',
                data: povertyHelper4.dec,
                itemStyle: {
                    color: '#90ca8f'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },{
                name: '2018/10',
                xAxisIndex: 1,
                yAxisIndex: 1,
                type: 'scatter',
                data: povertyHelper4.oct,
                itemStyle: {
                    color: '#90ca8f'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },{
                name: '2018/11',
                xAxisIndex: 1,
                yAxisIndex: 1,
                type: 'scatter',
                data: povertyHelper4.nov,
                itemStyle: {
                    color: '#90ca8f'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            }, {
                name: '2018/12',
                xAxisIndex: 1,
                yAxisIndex: 1,
                type: 'scatter',
                data: povertyHelper4.sept,
                itemStyle: {
                    color: '#90ca8f'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },{
                name: '2019/01',
                xAxisIndex: 1,
                yAxisIndex: 1,
                type: 'scatter',
                data: povertyHelper4.jan,
                itemStyle: {
                    color: '#90ca8f'
                },
                symbolSize: function (val) {
                    return val[2] / 3;
                }
            },
    ]};
    return (
        <Card>
            <Card.Header>
                <h4>4-2-2 消费总额对比及预警</h4>
                <Intro content={[
                    '设计理念: 以散点图的形式，展示学生日消费总额，点越大表示金额越高',
                    '功能: 比较贫困生与非贫困生的消费差异，同时有异常消费及时干预'
                ]} />
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-2 align-items-center'>
                        <span className='conclusion'><strong>第二步：</strong>选取部分贫困生样本和非贫困生样本，分别展示其消费总额情况，首先可以帮助校领导及时干预异常消费，其次也可以探究贫困生与非贫困生的消费差异</span>
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-9'>
                        <Ec option={option} h='400px' />
                    </div>
                </div>
            </Card.Body>
        </Card>
    )   
}
import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';

import povertyHelper1 from '../data/povertyHelper/PovertyHelper1.json'
import povertyHelper2 from '../data/povertyHelper/PovertyHelper2.json'

const normal_data_1 = povertyHelper1.normal
const poverty_data_1 = povertyHelper1.poverty
const normal_data_2 = povertyHelper2.normal
const poverty_data_2 = povertyHelper2.poverty

export default function() {
    const option = {
        grid: [{
            left: 0,
            right: '54%',
            top: '10%',
            bottom: 0,
            containLabel: true,
        }, {
            left: '54%',
            right: '8%',
            top: '10%',
            bottom: 0,
            containLabel: true,
        }],
        tooltip: {
            position: 'top',
            formatter: params => (
                [ '学生ID：' + params.data[2], '消费次数：' + parseInt(params.data[0]) + ' 次', '消费金额：' + parseInt(params.data[1]) + ' 元', ].join('<br/>')
            )
        },
        xAxis: [{
            name: '消费次数',
            type: 'value',
            axisTick: {show: false},
            splitLine: {
                lineStyle: {
                    type: 'dashed',
                    color: '#eeeeee',
                }
            },
            gridIndex: 0
        },{
            name: '消费次数',
            type: 'value',
            axisTick: {show: false},
            splitLine: {
                lineStyle: {
                    type: 'dashed',
                    color: '#eeeeee',
                }
            },
            gridIndex: 1
        }],
        yAxis: [{
            name: '消费总额',
            type: 'value',
            axisTick: {show: false},
            splitLine: {
                lineStyle: {
                    type: 'dashed',
                    color: '#eeeeee',
                }
            },
            gridIndex: 0
        },{
            name: '平均消费',
            type: 'value',
            axisTick: {show: false},
            splitLine: {
                lineStyle: {
                    type: 'dashed',
                    color: '#eeeeee',
                }
            },
            min: 0,
            max: 20,
            gridIndex: 1
        }],
        visualMap: [{
            seriesIndex: [2, 3],
            min: 4,
            max: 8,
            dimension: 1,
            inRange: {
                color: ['#df6b66', '#90ca8f'],
            },
            show: false
        }, {
            seriesIndex: [0, 1],
            min: 0,
            max: 2000,
            dimension: 1,
            inRange: {
                color: ['#df6b66', '#90ca8f'],
            },
            show: false
        }],
        series: [{
            xAxisIndex: 0,
            yAxisIndex: 0,
            symbolSize: 5,
            data: normal_data_1,
            type: 'scatter',
            itemStyle: {
                emphasis: {
                    borderColor: 'rgba(0, 0, 0, 0.5)',
                    borderWidth: 1.5
                }
            }
        },{
            xAxisIndex: 0,
            yAxisIndex: 0,
            symbolSize: 5,
            data: poverty_data_1,
            type: 'scatter',
            itemStyle: {
                emphasis: {
                    borderColor: 'rgba(0, 0, 0, 0.5)',
                    borderWidth: 1.5
                }
            }
        },{
            xAxisIndex: 1,
            yAxisIndex: 1,
            type: 'scatter',
            symbolSize: 5,
            data: normal_data_2,
            itemStyle: {
                emphasis: {
                    borderColor: 'rgba(0, 0, 0, 0.5)',
                    borderWidth: 1.5
                }
            }
        },{
            xAxisIndex: 1,
            yAxisIndex: 1,
            symbolSize: 5,
            type: 'scatter',
            data: poverty_data_2,
            itemStyle: {
                emphasis: {
                    borderColor: 'rgba(0, 0, 0, 0.5)',
                    borderWidth: 1.5
                }
            }
        }]
    }; 
    return (
        <Card>
            <Card.Header>
                <h4>4-2-1 贫困生群体发现</h4>
                <Intro content={[
                    '设计理念: 以散点图形式，展示学生消费的分布情况',
                    '功能: 帮助校领导层宏观掌握消费情况，发现贫困生群体'
                ]} />
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-2 align-items-center'>
                        <span className='conclusion'><strong>第一步：</strong>根据学生的消费次数、消费总额、平均消费三个维度的交叉验证，帮助校领导发现学校中的贫困群体</span>
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-9'>
                        <Ec option={option} h='360px' />
                    </div>
                </div>
            </Card.Body>
        </Card>
    )    
}
import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';

import povertyHelper7 from '../data/povertyHelper/PovertyHelper7.json'

const timeline = ['2018/09', '2018/10', '2018/11', '2018/12', '2019/01']

const studentID = povertyHelper7.studentID

const dataset = povertyHelper7.dataset

export default function() {
    const option = {
        baseOption: {
            timeline: {
                axisType: 'category',
                orient: 'vertical',
                autoPlay: true,
                inverse: true,
                playInterval: 3000,
                right: 0,
                top: '12%',
                bottom: 0,
                width: 70,
                height: null,
                label: {
                    normal: {
                        textStyle: {
                            color: '#999'
                        }
                    },
                    emphasis: {
                        textStyle: {
                            color: '#000'
                        }
                    }
                },
                lineStyle: {
                    color: '#555'
                },
                checkpointStyle: {
                    color: '#aaa',
                    borderColor: '#666',
                    borderWidth: 2
                },
                controlStyle: {
                    showNextBtn: false,
                    showPrevBtn: false,
                    normal: {
                        color: '#aaa',
                        borderColor: '#aaa'
                    },
                    emphasis: {
                        color: '#666',
                        borderColor: '#666'
                    }
                },
                data: timeline
            },
            tooltip: {
                formatter: function(params) {
                    return [
                        "学生ID：" + params.data[0],
                        "贫困指数：" + params.data[1]
                        ].join('<br/>')
                }
            },
            grid: {
                left: '2%',
                right: '15%',
                top: '12%',
                bottom: 0,
                containLabel: true,
            },
            xAxis: {
                name: '学号',
                axisTick: {show: false},
                data: studentID
            },
            yAxis: {
                type: 'value',
                name: '贫困指数',
                axisTick: {show: false},
                splitLine: {
                    lineStyle: {
                        type: 'dashed',
                        color: '#eeeeee'
                    }
                },
                min: 0,
                max: 30,
            },
            visualMap: {
                min: -3,
                max: 25,
                inRange: {
                    color: ['#227d51', '#fbe251', '#cb4042'],
                    symbolSize: [8, 16]
                },
                show: false
            },
            series: [{
                symbolSize: 6,
                data: dataset[0],
                type: 'scatter',
                itemStyle: {
                    normal: {
                        shadowColor: 'rgba(0 ,0, 0, 0.3)',
                        shadowBlur: 3
                    },
                },
                markArea: {
                    silent: true,
                    label: {
                        position: 'right',
                        fontSize: 12,
                        color: '#000'
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(189,192,186, 0.1)',
                        }
                    },
                    data: [[{
                        name: '特别困难',
                        xAxis: 'min',
                        yAxis: '20.5'
                    }, {
                        xAxis: 'max',
                        yAxis: '30'
                    }],[{
                        name: '困难',
                        xAxis: 'min',
                        yAxis: '10.5'
                    }, {
                        xAxis: 'max',
                        yAxis: '20'
                    }],[{
                        name: '一般困难',
                        xAxis: 'min',
                        yAxis: '0.5'
                    }, {
                        xAxis: 'max',
                        yAxis: '10'
                    }]]
                },
            }]
        },
        options: [{
            title: {
                text: "2018年09月",
                left: 'center',
                textStyle: {
                    fontWeight: 500,
                    fontSize: 15,
                }
            },
            series: {
                data: dataset[0],
            }
        },{
            title: {
                text: "2018年10月",
                left: 'center',
                textStyle: {
                    fontWeight: 500,
                    fontSize: 15,
                }
            },
            series: {
                data: dataset[1],
            }
        },{
            title: {
                text: "2018年11月",
                left: 'center',
                textStyle: {
                    fontWeight: 500,
                    fontSize: 15,
                }
            },
            series: {
                data: dataset[2]
            }
        },{
            title: {
                text: "2018年12月",
                left: 'center',
                textStyle: {
                    fontWeight: 500,
                    fontSize: 15,
                }
            },
            series: {
                data: dataset[3]
            }
        },{
            title: {
                text: "2019年01月",
                left: 'center',
                textStyle: {
                    fontWeight: 500,
                    fontSize: 15,
                }
            },
            series: {
                data: dataset[4]
            }
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>4-2-4 贫困指数综合评估</h4>
                <Intro content={[
                    '设计理念: 以散点图配合颜色编码的形式，展示贫困生贫困指数的变化情况',
                    '功能: 帮助校领导层针对不同等级贫困生进行帮扶'
                ]} />
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-2 align-items-center'>
                        <span className='conclusion'><strong>第四步：</strong>构建贫困指数分析模型，对贫困生的困难情况进行分级，以便针对不同等级的贫困生进行不同程度的帮扶</span>
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

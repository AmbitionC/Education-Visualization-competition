import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import jsonDateGender from '../data/consumption/school/date_gender.json';

export default function() {
    let maleMoney = [];
    let femaleMoney = [];
    let maleNum = [];
    let femaleNum = [];
    let maleMean = [];
    let femaleMean = [];
    for (let i = 0; i < jsonDateGender.data.length; i ++) {
        const singleData = jsonDateGender.data[i];
        if (singleData[1] + singleData[2] >= 1000) {
            const date = singleData[0].replace(/\//g, '-');
            maleMoney.push([date, singleData[4].toFixed(2)]);
            femaleMoney.push([date, singleData[5].toFixed(2)]);
            maleNum.push([date, singleData[1]]);
            femaleNum.push([date, singleData[2]]);
            maleMean.push([date, (singleData[4] / singleData[1]).toFixed(2)]);
            femaleMean.push([date, (singleData[5] / singleData[2]).toFixed(2)]);
        }
    }
    const option = {
        legend: {
            selectedMode: 'single'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                animation: false
            }
        },
        grid: [{
            left: '3%',
            right: '2%',
            top: '8.5%',
            height: '45%',
            containLabel: true
        }, {
            left: '3%',
            right: '2%',
            bottom: '8%',
            height: '45%',
            containLabel: true
        }],
        axisPointer: {
            link: {xAxisIndex: 'all'}
        },
        xAxis : [
            {
                type : 'time',
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                },
                axisLine: {
                    show: false
                }
            },
            {
                show: false,
                gridIndex: 1,
                type : 'time',
                position: 'top',
            }
        ],
        yAxis : [
            {
                name: '男生',
                type: 'value',
                // max: 30000,
                axisLabel: {
                    formatter: '{value}元'
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
            {
                name: '女生',
                gridIndex: 1,
                type: 'value',
                inverse: true,
                // max: 30000,
                axisLabel: {
                    formatter: '{value}元'
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
            {
                type: 'value',
                max: 1000,
                axisLabel: {
                    formatter: '{value}人'
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
            {
                gridIndex: 1,
                type: 'value',
                inverse: true,
                max: 1000,
                axisLabel: {
                    formatter: '{value}人'
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
            }
        ],
        series : [
            {
                name:'消费总额',
                type:'line',
                smooth: true,
                areaStyle: {
                    opacity: 1,
                },
                itemStyle: {
                    color: '#749aa0',
                },
                showSymbol: false,
                hoverAnimation: false,
                data: maleMoney,
            },
            {
                name:'消费总额',
                type:'line',
                xAxisIndex: 1,
                yAxisIndex: 1,
                smooth: true,
                areaStyle: {
                    opacity: 1,
                },
                itemStyle: {
                    color: '#df6b66',
                },
                showSymbol: false,
                hoverAnimation: false,
                data: femaleMoney,
            },
            {
                name:'消费人数',
                type:'line',
                xAxisIndex: 0,
                yAxisIndex: 2,
                smooth: true,
                areaStyle: {
                    opacity: 1,
                },
                itemStyle: {
                    color: '#749aa0',
                },
                showSymbol: false,
                hoverAnimation: false,
                data: maleNum,
            },
            {
                name:'消费人数',
                type:'line',
                xAxisIndex: 1,
                yAxisIndex: 3,
                smooth: true,
                areaStyle: {
                    opacity: 1,
                },
                itemStyle: {
                    color: '#df6b66',
                },
                showSymbol: false,
                hoverAnimation: false,
                data: femaleNum,
            },
            {
                name:'人均金额',
                type:'line',
                smooth: true,
                areaStyle: {
                    opacity: 1,
                },
                itemStyle: {
                    color: '#749aa0',
                },
                showSymbol: false,
                hoverAnimation: false,
                data: maleMean,
            },
            {
                name:'人均金额',
                type:'line',
                xAxisIndex: 1,
                yAxisIndex: 1,
                smooth: true,
                areaStyle: {
                    opacity: 1,
                },
                itemStyle: {
                    color: '#df6b66',
                },
                showSymbol: false,
                hoverAnimation: false,
                data: femaleMean,
            },
        ]
    };
    return (
        <Card>
            <Card.Header>
                <h4>1-5-4 消费对比</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='360px'/>
            </Card.Body>
        </Card>
    );
}
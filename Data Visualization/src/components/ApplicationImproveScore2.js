import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'
import Intro from './Intro';
import jsonData from '../data/app/mean_std.json';
import jsonData2 from '../data/app/stability.json';

export default function() {
    const option = {
        legend: {},
        grid: {
            left: 0,
            right: '12%',
            top: '18%',
            bottom: 0,
            containLabel: true 
        },
        xAxis: {
            name: '平均分',
            min: 40,
            max: 100,
            axisTick: {
                show: false
            },
            splitLine: {
                show: false,
            }
        },
        yAxis: {
            name: '标准差',
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            },
        },
        series: [{
            name: '成绩稳定学生群体',
            type: 'scatter',
            symbolSize: 3,
            data: jsonData[0],
            itemStyle: {
                color: '#90ca8f',
            }
        }, {
            name: '成绩不稳定学生群体',
            type: 'scatter',
            symbolSize: 3,
            data: jsonData[1],
            itemStyle: {
                color: '#df6b66',
            }

        }, {
            name: '其他群体',
            type: 'scatter',
            symbolSize: 3,
            data: jsonData[-1],
            itemStyle: {
                color: '#c0c0c0',
            }
        }]
    };
    const option2 = {
        tooltip: {
            formatter: params => {
                const res = [
                    '学号: ' + params.data[2],
                    params.data[3],
                    '不稳定指标: ' + params.data[4].toFixed(2)
                ]
                return res.join('<br/>');
            }
        },
        grid: {
            left: 0,
            right: 0,
            top: 0,
            bottom: '6%',
            containLabel: true 
        },
        xAxis: {
            name: '学号',
            nameLocation: 'center',
            nameGap: 5,
            type: 'category',
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false,
            }
        },
        yAxis: {
            type: 'category',
            data: ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术'],
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
        },
        visualMap: {
            show: false,
            min: 0,
            max: 35,
            range: [0, 15],
            inRange: {
                color: '#90ca8f',
                opacity: [0.1, 1]
            },
            outOfRange: {
                color: '#df6b66',
                opacity: [0.1, 1]
            }
        },
        series: [{
            type: 'heatmap',
            data: jsonData2.data,
            itemStyle: {
                emphasis: {
                    color: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>4-1-2 探究成绩稳定性</h4>
                <Intro content={[
                    '左图: 以散点图的形式，展示学生分布情况，通过聚类将学生分为3类群体',
                    '右图: 以热力图的形式，展示在成绩不稳定学生群体中的学生各学科的成绩不稳定性',
                ]} />
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-4'>
                        <Ec option={option} h='360px' />
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-4'>
                        <Ec option={option2} h='360px' />
                    </div>
                    <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                        <div className='right-arrow'></div>
                    </div>
                    <div className='col-12 col-lg-2 align-items-center'>
                        <span className='conclusion'><strong>结论：</strong>学校中有部分学生，其成绩中等偏上，但成绩极不稳定，他们有着很大的提升空间，需要班主任、科任教师和校领导高度重视</span>
                    </div>
                </div>
            </Card.Body>
        </Card>
    );
}

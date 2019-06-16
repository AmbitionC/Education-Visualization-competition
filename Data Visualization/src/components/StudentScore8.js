import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'
import StudentScore from '../data/student/Student_Score_6.json'

// 展示学生的各个学科的成绩和排名，使用不同的legend表示，其中包含成绩包含班级的平均分，排名包含预测
const xlabel = StudentScore.xlabel;
const sub_rank = StudentScore.sub_rank;
const sub_rank_predict = StudentScore.sub_rank_predict;
const sub_rank_down = StudentScore.sub_rank_down;
const sub_rank_up = StudentScore.sub_rank_up;

export default function(){
    const option = {
        legend: {
            data: ['历史排名', '预测排名', '置信区间'],
            right: 'right'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'line'
            },
            formatter: (params) => {
                if (params.length === 1) {
                    return params[0].name + '<br/>' + params[0].marker + params[0].data + '名';
                }
                return params[1].name + '<br/>' + params[1].marker + params[1].seriesName + ': ' + params[1].data + '<br/>' + params[2].marker + '置信区间: ' + params[2].data + '名~' + (params[2].data + params[3].data) + '名';
            }
        },
        grid:{
            left: 0,
            right: 0,
            top: '20%',
            bottom: '5%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false
            },
            data: xlabel
        },
        yAxis: {
            name: '排名',
            nameLocation: 'start',
            min: 1,
            max: 50,
            inverse: true,
            type: 'value',
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
        series: [{
            name: '预测排名',
            data: sub_rank_predict,
            itemStyle: {
                color: '#df6b66'
            },
            type: 'line'
        },{
            name: '历史排名',
            data: sub_rank,
            itemStyle: {
                color: '#7189aa'
            },
            type: 'line'
        },{
            name: '置信区间',
            data: sub_rank_down,
            type: 'line',
            itemStyle: {
                color: '#bdc0ba',
            },
            lineStyle: {
                    normal: {
                        opacity: 0
                    }
                },
                stack: 'confidence-band',
        },{
            name: '置信区间',
            data: sub_rank_up,
            type: 'line',
            itemStyle: {
                color: '#bdc0ba',
            },
            lineStyle: {
                    normal: {
                        opacity: 0
                    }
                },
                areaStyle: {
                    normal: {
                        color: '#ccc'
                    }
                },
                stack: 'confidence-band',
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>3-4 生物排名趋势</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='180px' />
            </Card.Body>
        </Card>
    )
}
import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';

export default function() {
    const option = {
        color: ['#8cc1aa', '#df6b66', '#7189aa'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            }
        },
        grid: {
            left: 0,
            right: 0,
            top: '2%',
            bottom: '8%',
            containLabel: true
        },
        legend: {
            bottom: 'bottom',
            data:['男生','女生','总人数']
        },
        xAxis: {
                type: 'category',
                axisTick: {
                    show: false
                },
                data: ['≤15岁','16岁','17岁','18岁','19岁','≥20岁']
        },
        yAxis: {
                type: 'value',
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
        series: [
            {
                name:'男生',
                type:'bar',
                data:[2, 254, 313, 232, 96, 0]
            },
            {
                name:'女生',
                type:'bar',
                data:[5, 174, 253, 241, 111, 1]
            },
            {
                name:'总人数',
                type:'line',
                data:[7, 428, 566, 473, 207, 1]
            }
        ]
    };
    return (
        <Card>
            <Card.Header>
                <h4>1-1-1 年龄分布</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='300px'/>
            </Card.Body>
        </Card>
    );
}


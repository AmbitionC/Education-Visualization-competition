import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';

const Score_1 = [40, 23, 33, 32, 40, 40, 42, 40, 41];
const Score_2 = [33, 31, 37, 35, 39, 41, 41, 39, 40];
const Score_3 = [34, 32, 39, 19, 29, 41, 40, 39, 40];

export default function(){
    const option = {
        tooltip: {},
        legend: {
            data: ['期中考试', '平时成绩', '期末考试'],
            bottom: 'bottom',
            selected: {
                '期中考试': true,
                '平时成绩': false,
                '期末考试': false
            }
        },
        radar: {
            name: {
                textStyle: {
                    color: '#fff',
                    backgroundColor: '#91989f',
                    borderRadius: 5,
                    padding: [3, 5]
               }
            },
            axisLine: {
                lineStyle: {
                    color: '#bdc0ba'
                }
            },
            splitNumber: 3,
            splitLine: {
                lineStyle: {
                    color: '#bdc0ba'
                }
            },
            splitArea: {
                show: false
            },
            inverse: true,
            indicator: [
               { name: '语文', max: 50, min: 1},
               { name: '数学', max: 50, min: 1},
               { name: '英语', max: 50, min: 1},
               { name: '物理', max: 50, min: 1},
               { name: '化学', max: 50, min: 1},
               { name: '生物', max: 50, min: 1},
               { name: '政治', max: 50, min: 1},
               { name: '历史', max: 50, min: 1},
               { name: '地理', max: 50, min: 1}
            ]
        },
        series: [{
            type: 'radar',
            areaStyle: {normal: {
                color: '#749aa0',
                opacity: 0.3
            }},
            itemStyle: {
                color: '#749aa0'
            },
            data: [{
                value: Score_1,
                name: '期中考试'
                
            }]
        },{
            type: 'radar',
            areaStyle: {normal: {
                opacity: 0.3,
                color: '#df6b66'
            }},
            itemStyle: {
                color: '#df6b66'
            },
            data: [{
                value: Score_2,
                name: '平时成绩'
                
            }]
            
        },{
            type: 'radar',
            areaStyle: {normal: {
                color: '#91b493',
                opacity: 0.3
            }},
            itemStyle: {
                color: '#91b493'
            },
            data: [{
                value: Score_3,
                name: '期末考试'
                
            }]
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>3-2 学科排名雷达图</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='453px'/>
            </Card.Body>
        </Card>
    )
}
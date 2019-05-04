import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'

export default function() {
    const option = {
        tooltip: {
            formatter: '选择{b0}人数占比：{c0}%'
        },
        xAxis: {
            type: 'category',
            name: '学科名',
            data: ['生物', '政治', '物理', '化学', '地理', '历史', '技术']
        },
        yAxis: {
            name:'百分比 %',
            type: 'value'
        },
        series: [{
            data: [19.25, 18.623, 15.63, 15.53, 14.44, 13.82, 2.70],
            itemStyle: {
                color: '#ff9797',
            },
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
            type: 'bar'
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>单科选择排名</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='250px'/>
            </Card.Body>
        </Card>
    )
}
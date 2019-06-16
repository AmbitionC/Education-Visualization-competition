import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'

export default function() {
    const option = {
        color: ['#7189aa', '#df6b66', '#e79d88', '#8cc1aa', '#749aa0', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
        series: [
            {
                type:'pie',
                radius: [0, '60%'],
                hoverAnimation: false,
                label: {
                    formatter: '{b}\n{c}%'
                },
                data:[
                    {value: 15.63, name: '物理'},
                    {value: 15.53, name: '化学'},
                    {value: 19.25, name: '生物'},
                    {value: 18.625, name: '政治'},
                    {value: 13.82, name: '历史'},
                    {value: 14.44, name: '地理'},
                    {value: 2.70, name: '技术'},
                ]
            }
        ]
    };
    return (
        <Card>
            <Card.Header>
                <h4>4-3-2 单学科选择比例</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='240px'/>
            </Card.Body>
        </Card>
    )
}
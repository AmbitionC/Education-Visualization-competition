import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'

export default function() {
    const option = {
        tooltip: {
            formatter: '选择{b0}组合占比：{c0}%'
        },
        grid: {
            left: 0,
            right: '2%',
            top: '15%',
            bottom: 0,
            containLabel: true
        },
        xAxis: {
            type: 'category',
            axisTick: {
                show: false
            },
            data: ['物理+化学+生物', '物理+政治+生物', '化学+政治+生物', '物理+化学+政治', '物理+生物+地理', '物理+历史+生物', '化学+生物+地理', '化学+历史+生物', '政治+生物+地理', '政治+历史+生物', '物理+化学+地理', '物理+化学+历史', '物理+政治+地理', '物理+政治+历史', '化学+政治+地理', '化学+政治+历史', '历史+生物+地理', '物理+历史+地理', '化学+历史+地理', '政治+历史+地理', '物理+生物+技术', '化学+生物+技术', '政治+生物+技术', '物理+化学+技术', '物理+政治+技术', '化学+政治+技术', '生物+地理+技术', '历史+生物+技术', '物理+地理+技术', '物理+历史+技术', '化学+地理+技术', '化学+历史+技术', '政治+地理+技术', '政治+历史+技术', '历史+地理+技术'].map((items, index)=>{
                return items.replace(/\+/g, '\n');
            })
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value}%'
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
        // dataZoom: [{
        //     show: true,
        //     start: 30,
        //     end: 65,
        // },{
        //     type: 'inside',
        //     start: 30,
        //     end: 65
        // }],
        series: {
            data: [3.69, 3.68, 3.66, 3.45, 3.41, 3.39, 3.38, 3.37, 3.37, 3.36, 3.17, 3.16, 3.16, 3.15, 3.14, 3.12, 3.08, 2.87, 2.85, 2.84, 2.68, 2.66, 2.65, 2.45, 2.44, 2.42, 2.38, 2.36, 2.16, 2.15, 2.14, 2.13, 2.13, 2.12, 1.84],
            type: 'bar',
            itemStyle: {
                color: '#749aa0',
            },
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                ]
            },
        }
    }; 
    return (
        <Card>
            <Card.Header>
                <h4>4-3-4 三学科选择比例</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='240px'/>
            </Card.Body>
        </Card>
    )
}
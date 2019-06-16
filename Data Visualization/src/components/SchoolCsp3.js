import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import jsonData from '../data/consumption/school/time_peo_num.json';

const getTimeData = (oriData, type) => {
    let res = [];
    if (type === 'am') {
        for (let i = 0; i < oriData.length; i ++) {
            if (oriData[i][1] < 24) {
                oriData[i][0] -= 1;
                res.push(oriData[i]);
            }
        }
    }
    if (type === 'pm') {
        for (let i = 0; i < oriData.length; i ++) {
            if (oriData[i][1] >= 24) {
                oriData[i][0] -= 1;
                res.push(oriData[i]);
            }
        }
    }
    return res;
};

const renderItemForTimeNum = (params, api) => {
    const values = [api.value(0), api.value(1)];
    const coord = api.coord(values);
    const size = api.size([1, 1], values);
    return {
        type: 'sector',
        shape: {
            cx: params.coordSys.cx,
            cy: params.coordSys.cy,
            r0: coord[2] - size[0] / 2,
            r: coord[2] + size[0] / 2,
            startAngle: -(coord[3] + size[1] / 1000),
            endAngle: -(coord[3] - size[1] / 1)
        },
        style: api.style({
            fill: api.visual('color')
        }),
        styleEmphasis: api.styleEmphasis()
    };
};

export default function() {
    const option= {
        legend: {
            top: 'top',
            right: 'right',
            orient: 'vertical',
            selectedMode: 'single',
        },
        polar: {},
        tooltip: {
            formatter: (params) => {
                return '第' + (params.data[0] + 1) + '周<br />消费人数: ' + params.data[2];
            },
        },
        visualMap: {
            show: false,
            type: 'continuous',
            min: 0,
            max: 5000,
            range: [1, 5000],
            inRange: {
                color: ['#fff5f5', '#df6b66'],
            },
            outOfRange: {
                color: '#ffffff'
            }
        },
        angleAxis: {
            type: 'category',
            data: ['12', '', '1', '', '2', '', '3', '', '4', '','5','', '6', '', '7', '', '8', '', '9', '', '10', '', '11', ''],
            boundaryGap: false,
        },
        radiusAxis: {
            show: false,
            type: 'category',
            data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
        },
        series: [{
            name: 'AM',
            type: 'custom',
            coordinateSystem: 'polar',
            legendHoverLink: false,
            itemStyle: {
                normal: {
                    color: '#df6b66'
                },
                emphasis: {
                    borderColor: '#bdc0ba'
                },
            },
            renderItem: renderItemForTimeNum,
            data: getTimeData(jsonData.data, 'am'),
        }, {
            name: 'PM',
            type: 'custom',
            coordinateSystem: 'polar',
            legendHoverLink: false,
            itemStyle: {
                normal: {
                    color: '#df6b66'
                },
                emphasis: {
                    borderColor: '#bdc0ba'
                },
            },
            renderItem: renderItemForTimeNum,
            data: getTimeData(jsonData.data, 'pm'),
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>1-5-3 消费高峰时刻</h4>
                <Intro content={[
                    '设计理念: 通过钟表的形式显示学校的消费高峰',
                    '功能: 帮助校领导针对不同的时段作出相应安排，达到最大化利用学校资源'
                ]} />
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='280px'/>
            </Card.Body>
        </Card>
    );
}
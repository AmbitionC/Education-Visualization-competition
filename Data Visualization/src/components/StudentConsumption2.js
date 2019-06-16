import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'

const hours = [ '0点', '1点', '2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点','10点','11点', '12点', '13点', '14点', '15点', '16点', '17点', '18点', '19点', '20点', '21点', '22点', '23点'];
const days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日'];
const dataset = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 17], [0, 7, 2], [0, 8, 0], [0, 9, 0], [0, 10, 2], [0, 11, 9], [0, 12, 13], [0, 13, 0], [0, 14, 0], [0, 15, 0], [0, 16, 2], [0, 17, 8], [0, 18, 0], [0, 19, 0], [0, 20, 0], [0, 21, 0], [0, 22, 0], [0, 23, 0], [1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 22], [1, 7, 3], [1, 8, 0], [1, 9, 0], [1, 10, 0], [1, 11, 12], [1, 12, 10], [1, 13, 0], [1, 14, 0], [1, 15, 0], [1, 16, 0], [1, 17, 12], [1, 18, 3], [1, 19, 0], [1, 20, 0], [1, 21, 0], [1, 22, 0], [1, 23, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 21], [2, 7, 8], [2, 8, 0], [2, 9, 0], [2, 10, 0], [2, 11, 9], [2, 12, 18], [2, 13, 0], [2, 14, 0], [2, 15, 0], [2, 16, 0], [2, 17, 18], [2, 18, 0], [2, 19, 0], [2, 20, 0], [2, 21, 0], [2, 22, 0], [2, 23, 0], [3, 0, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [3, 6, 16], [3, 7, 8], [3, 8, 0], [3, 9, 0], [3, 10, 1], [3, 11, 6], [3, 12, 24], [3, 13, 0], [3, 14, 0], [3, 15, 0], [3, 16, 0], [3, 17, 23], [3, 18, 1], [3, 19, 0], [3, 20, 0], [3, 21, 0], [3, 22, 0], [3, 23, 0], [4, 0, 0], [4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [4, 6, 16], [4, 7, 8], [4, 8, 0], [4, 9, 0], [4, 10, 1], [4, 11, 4], [4, 12, 25], [4, 13, 0], [4, 14, 0], [4, 15, 1], [4, 16, 1], [4, 17, 22], [4, 18, 1], [4, 19, 0], [4, 20, 0], [4, 21, 0], [4, 22, 0], [4, 23, 0], [5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0], [5, 6, 22], [5, 7, 9], [5, 8, 0], [5, 9, 0], [5, 10, 4], [5, 11, 5], [5, 12, 27], [5, 13, 0], [5, 14, 0], [5, 15, 0], [5, 16, 3], [5, 17, 19], [5, 18, 0], [5, 19, 0], [5, 20, 0], [5, 21, 0], [5, 22, 0], [5, 23, 0], [6, 0, 0], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 18], [6, 7, 4], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 5], [6, 12, 15], [6, 13, 0], [6, 14, 0], [6, 15, 0], [6, 16, 3], [6, 17, 23], [6, 18, 0], [6, 19, 0], [6, 20, 0], [6, 21, 0], [6, 22, 0], [6, 23, 0]];

function renderItem(params, api) {
    var values = [api.value(0), api.value(1)];
    var coord = api.coord(values);
    var size = api.size([1, 1], values);
    return {
        type: 'sector',
        shape: {
            cx: params.coordSys.cx,
            cy: params.coordSys.cy,
            r0: coord[2] - size[0] / 2,
            r: coord[2] + size[0] / 2,
            startAngle: -(coord[3] + size[1] / 2),
            endAngle: -(coord[3] - size[1] / 2)
        },
        style: api.style({
            fill: api.visual('color')
        })
    };
}

export default function(){
    const option = {
        polar: {},
        tooltip: {
            axisPointer: {
                type: 'cross'
            } ,
            formatter: (params) => {
                const weekdayArr = ['一', '二', '三', '四', '五', '六', '日'];
                return '周' + weekdayArr[params.data[0]] + '<br/>' + params.data[1] + ':00-' + (params.data[1]+1) + ':00<br/>消费' + params.data[2] + '次';
            }
        },
        visualMap: {
            show: false,
            type: 'continuous',
            range: [1, 30],
            min: 0,
            max: 30,
            top: 'middle',
            dimension: 2,
            calculable: true,
            inRange: {
                color: '#df6b66',
                opacity: [0.1, 1]
            },
            outRange: {
                color: '#ffffff'
            }
        },
        angleAxis: {
            type: 'category',
            data: hours,
            boundaryGap: true,
            splitLine: {
                show: false,
            },
            axisTick: {
                show: false
            }
        },
        radiusAxis: {
            type: 'category',
            data: days,
            z: 100,
            axisTick: {
                show: false
            }
        },
        series: [{
            type: 'custom',
            coordinateSystem: 'polar',
            itemStyle: {
                normal: {
                    color: '#d14a61'
                }
            },
            renderItem: renderItem,
            data: dataset
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>3-7 学生消费习惯</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h = '300px'/>
            </Card.Body>
        </Card> 
    )
}
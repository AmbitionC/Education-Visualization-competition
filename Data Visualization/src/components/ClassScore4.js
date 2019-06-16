import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import jsonData from '../data/grade/class/class920_sub_trend.json';

export default class extends React.Component {
    constructor(props) {
        super(props);
        this.option = null;
    }
    componentWillMount() {
        let series = [];
        for (let subName in jsonData) {
            series.push({
                name: subName,
                type:'line',
                itemStyle: {
                    color: '#df6b66'
                },
                areaStyle: {
                    opacity: 1
                },
                smooth: true,
                showSymbol: false,
                data: jsonData[subName][0]
            });
            series.push({
                name: subName,
                type:'line',
                itemStyle: {
                    color: '#df6b66'
                },
                areaStyle: {
                    color: '#fff',
                    opacity: 1
                },
                smooth: true,
                showSymbol: false,
                data: jsonData[subName][1]
            });
            series.push({
                name: subName,
                type:'line',
                itemStyle: {
                    color: '#ffffff',
                },
                lineStyle: {
                    width: 1,
                    opacity: 0.4
                },
                smooth: true,
                showSymbol: false,
                data: jsonData[subName][2]
            });
        }
        this.option = {
            legend: {
                type: 'scroll',
                selectedMode: 'single',
                bottom: 'bottom',
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    axis: 'x',
                    type: 'line'
                },
                formatter: (params) => {
                    let res = '';
                    res += params[0].marker + '最高分: ' + params[0].data.toFixed(2) + '<br/>';
                    res += params[2].marker +'平均分: ' + params[2].data.toFixed(2) + '<br/>';
                    res += params[1].marker +'最低分: ' + params[1].data.toFixed(2);
                    return res;
                }
            },
            grid: {
                left: 0,
                right: 0,
                top: 0,
                bottom: '24%',
            },
            xAxis: {
                type: 'category',
                show: false,
                boundaryGap : false,
                data: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            },
            yAxis: {
                show: false
            },
            series: series
        };
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>2-1 成绩趋势</h4>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option} h='160px'/>
                </Card.Body>
            </Card>
        );
    }
}

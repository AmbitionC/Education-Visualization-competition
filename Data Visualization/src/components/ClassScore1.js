import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import associateJson from '../data/grade/class/class920_associate_sub.json';

export default class extends React.Component {
    constructor(props) {
        super(props);
        this.option = null;
    }
    componentWillMount() {
        const xData = ['60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'];
        const yData = ['体育', '音乐', '美术'];
        const data = associateJson.data;
        this.option = {
            color: ['#749aa0', '#df6b66', '#e79d88', '#8cc1aa', '#ec7e55', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
            grid: {
                left: 0,
                right: 0,
                top: '15%',
                bottom: 0,
                containLabel: true
            },
            legend: {
                selectedMode: 'single',
            },
            tooltip: {
                formatter: (params) => {
                    const t = ['体育', '音乐', '美术'];
                    return t[params.data[1]] + (params.data[0] + 60) + '分: ' + params.data[2] + '人';
                }
            },
            xAxis: {
                type: 'category',
                data: xData,
            },
            yAxis: {
                type: 'category',
                data: yData,
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#eee',
                        type: 'dashed'
                    }
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
            },
            series: [{
                name: '2016-2017-1',
                type: 'scatter',
                symbolSize: function (val) {
                    return val[2] * 3;
                },
                data: data.slice(0, 53),
            }, {
                name: '2016-2017-2',
                type: 'scatter',
                symbolSize: function (val) {
                    return val[2] * 3;
                },
                data: data.slice(53, 87),

            }, {
                name: '2017-2018-1',
                type: 'scatter',
                symbolSize: function (val) {
                    return val[2] * 3;
                },
                data: data.slice(87, 112),

            }, {
                name: '2017-2018-2',
                type: 'scatter',
                symbolSize: function (val) {
                    return val[2] * 3;
                },
                data: data.slice(112, 136),

            }, {
                name: '2018-2019-1',
                type: 'scatter',
                symbolSize: function (val) {
                    return val[2] * 3;
                },
                data: data.slice(136),
            }]
        };
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>2-4 考查课</h4>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option} h='240px'/>
                </Card.Body>
            </Card>
        );
    }
}

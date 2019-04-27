import React from 'react';
import Ec from './Ec';
import associateJson from '../data/grade/class_associate_sub.json';

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
                        color: '#999',
                        type: 'dashed'
                    }
                },
                axisLine: {
                    show: false
                }
            },
            series: [{
                type: 'scatter',
                symbolSize: function (val) {
                    if (val[2] < 20) {
                        return val[2] * 4
                    }
                    return val[2] * 2;
                },
                data: data,
            }]
        };
    }
    render() {
        return (
            <div>
                <Ec option={this.option} h='400px'/>
            </div>
        );
    }
}

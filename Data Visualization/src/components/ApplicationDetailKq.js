import React from 'react';
import { Table , Input , Button , Icon } from 'antd';
import Highlighter from 'react-highlight-words';
import jsonData from '../data/ori_data/kq.json';
 
export default class extends React.Component {
    state = {
        searchText: '',
    };
    getColumnSearchProps = (dataIndex) => ({
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
        <div style={{ padding: 8 }}>
            <Input
            ref={node => { this.searchInput = node; }}
            value={selectedKeys[0]}
            onChange={e => setSelectedKeys(e.target.value ? [e.target.value] : [])}
            onPressEnter={() => this.handleSearch(selectedKeys, confirm)}
            style={{ width: 188, marginBottom: 8, display: 'block' }}
            />
            <Button
            type="primary"
            onClick={() => this.handleSearch(selectedKeys, confirm)}
            icon="search"
            size="small"
            style={{ width: 90, marginRight: 8 }}
            >
            查找
            </Button>
            <Button
            onClick={() => this.handleReset(clearFilters)}
            size="small"
            style={{ width: 90 }}
            >
            重置
            </Button>
        </div>
        ),
        filterIcon: filtered => <Icon type="search" style={{ color: filtered ? '#1890ff' : undefined }} />,
        onFilter: (value, record) => record[dataIndex].toString().toLowerCase().includes(value.toLowerCase()),
        onFilterDropdownVisibleChange: (visible) => {
        if (visible) {
            setTimeout(() => this.searchInput.select());
        }
        },
        render: (text) => (
        <Highlighter
            highlightStyle={{ backgroundColor: '#ffc069', padding: 0 }}
            searchWords={[this.state.searchText]}
            autoEscape
            textToHighlight={text?text:' '.toString()}
        />
        ),
    })

    handleSearch = (selectedKeys, confirm) => {
        confirm();
        this.setState({ searchText: selectedKeys[0] });
    }

    handleReset = (clearFilters) => {
        clearFilters();
        this.setState({ searchText: '' });
    }

    render() {
        const columns = [{
            title: 'ID',
            dataIndex: 'stu_id',
            key: 'stu_id',
            width: '7%',
            ...this.getColumnSearchProps('stu_id'),
        }, {
            title: '姓名',
            dataIndex: 'stu_name',
            key: 'stu_name',
            width: '7%',
            ...this.getColumnSearchProps('stu_name'),
        }, {
            title: '班级ID',
            dataIndex: 'cla_id',
            key: 'cla_id',
            width: '8%',
            ...this.getColumnSearchProps('cla_id'),
        }, {
            title: '班级名',
            dataIndex: 'cla_name',
            key: 'cla_name',
            width: '8%',
            ...this.getColumnSearchProps('cla_name'),
        }, {
            title: '学期',
            dataIndex: 'term',
            key: 'term',
            width: '12%',
            ...this.getColumnSearchProps('term'),
        }, {
            title: '考勤时间',
            dataIndex: 'time',
            key: 'time',
            width: '16%',
            ...this.getColumnSearchProps('time'),
        }, {
            title: '考勤ID',
            dataIndex: 'kaoqing_id',
            key: 'kaoqing_id',
            width: '8%',
            ...this.getColumnSearchProps('kaoqing_id'),
        }, {
            title: '考勤类型ID',
            dataIndex: 'kaoqintype_id',
            key: 'kaoqintype_id',
            width: '9%',
            ...this.getColumnSearchProps('kaoqintype_id'),
        }, {
            title: '考勤类型',
            dataIndex: 'kaoqintype_name',
            key: 'kaoqintype_name',
            width: '16%',
            ...this.getColumnSearchProps('kaoqintype_name'),
        }, {
            title: '考勤事件ID',
            dataIndex: 'control_task_order_id',
            key: 'control_task_order_id',
            width: '9%',
            ...this.getColumnSearchProps('control_task_order_id'),
        }];
        return <Table columns={columns} dataSource={jsonData} />;
    }
}

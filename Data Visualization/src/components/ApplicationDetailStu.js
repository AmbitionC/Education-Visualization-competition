import React from 'react';
import { Table , Input , Button , Icon } from 'antd';
import Highlighter from 'react-highlight-words';
import jsonData from '../data/ori_data/stu.json';
 
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
            textToHighlight={text.toString()}
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
            width: '6%',
            ...this.getColumnSearchProps('stu_id'),
        }, {
            title: '姓名',
            dataIndex: 'stu_name',
            key: 'stu_name',
            width: '6%',
            ...this.getColumnSearchProps('stu_name'),
        }, {
            title: '性别',
            dataIndex: 'gender',
            key: 'gender',
            width: '5%',
            ...this.getColumnSearchProps('gender'),
        }, {
            title: '出生年份',
            dataIndex: 'born_date',
            key: 'born_date',
            width: '6%',
            ...this.getColumnSearchProps('born_date'),
        }, {
            title: '民族',
            dataIndex: 'nation',
            key: 'nation',
            width: '6%',
            ...this.getColumnSearchProps('nation'),
        }, {
            title: '生源地',
            dataIndex: 'native_place',
            key: 'native_place',
            width: '7%',
            ...this.getColumnSearchProps('native_place'),
        }, {
            title: '家庭类型',
            dataIndex: 'residence_type',
            key: 'residence_type',
            width: '10%',
            ...this.getColumnSearchProps('residence_type'),
        }, {
            title: '政治面貌',
            dataIndex: 'policy',
            key: 'policy',
            width: '8%',
            ...this.getColumnSearchProps('policy'),
        }, {
            title: '班级ID',
            dataIndex: 'cla_id',
            key: 'cla_id',
            width: '7%',
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
            title: '是否住宿',
            dataIndex: 'zhusu',
            key: 'zhusu',
            width: '6%',
            ...this.getColumnSearchProps('zhusu'),
        }, {
            title: '寝室号',
            dataIndex: 'qinshihao',
            key: 'qinshihao',
            width: '7%',
            ...this.getColumnSearchProps('qinshihao'),
        }, {
            title: '是否退学',
            dataIndex: 'tuixue',
            key: 'tuixue',
            width: '8%',
            ...this.getColumnSearchProps('tuixue'),
        }];
        return <Table columns={columns} dataSource={jsonData} />;
    }
}

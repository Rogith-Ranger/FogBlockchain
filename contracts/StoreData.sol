pragma solidity ^0.4.24;

contract StoreData {
    struct currentData{
        uint ldata;
    }
    mapping(string => currentData[]) mainData;
    mapping(string=>uint) macCount;
    event addEvent (
    	string _mac
    	);
    constructor(){
        addData("00:0a:95:9d:68:16",123);
        addData("00:0a:95:9d:68:16",224);
        addData("00:0a:95:9d:68:16",214);
        addData("00:0a:95:9d:68:16",204);
        addData("00:0a:95:9d:68:16",234);
        addData("00:0b:25:3d:62:16",4);
        addData("00:0b:25:3d:62:16",423);
    }
    function addData (string memory _mac,uint _ldata) public {
        macCount[_mac]++;
        mainData[_mac].push(currentData(_ldata));
		emit addEvent(_mac);
    }
    function getCount(string memory _mac) public returns(uint){
        return macCount[_mac];
    }
    function getData(string memory _mac,uint i) public returns(uint){
        return mainData[_mac][i].ldata;
    }
}

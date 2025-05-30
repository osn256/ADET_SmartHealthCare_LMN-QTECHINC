// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HealthcareMonitor {
    struct Record {
        uint256 timestamp;
        string patientId;
        string heartRate;
        string bloodPressure;
        uint8 oxygenLevel;
        uint8 bodyTemp;            // Body temperature in Celsius, e.g., 37 for 37.0°C  to resolve the issues on decimal not showing 
        uint256 ecgPeakCount;
        uint256 ecgSignalStrength; // Multiplied by 100 for precision, e.g., 98 represents 0.98
        bool hasECG;
    }

    mapping(uint256 => Record) public records;
    uint256 public recordCount = 0;

    event RecordAdded(uint256 indexed id, string patientId);

    function addRecord(
        string memory _patientId,
        string memory _heartRate,
        string memory _bloodPressure,
        uint8 _oxygenLevel,
        uint8 _bodyTemp,
        uint256 _ecgPeakCount,
        uint256 _ecgSignalStrength, // e.g., 98 for 0.98
        bool _hasECG
    ) public {
        records[recordCount] = Record({
            timestamp: block.timestamp,
            patientId: _patientId,
            heartRate: _heartRate,
            bloodPressure: _bloodPressure,
            oxygenLevel: _oxygenLevel,
            bodyTemp: _bodyTemp,
            ecgPeakCount: _hasECG ? _ecgPeakCount : 0,
            ecgSignalStrength: _hasECG ? _ecgSignalStrength : 0,
            hasECG: _hasECG
        });

        emit RecordAdded(recordCount, _patientId);
        recordCount++;
    }

    function getRecord(uint256 _id) public view returns (Record memory) {
        require(_id < recordCount, "Record not found");
        return records[_id];
    }
}

import 'package:flutter/material.dart';
import 'package:flutter_bluetooth/flutter_bluetooth.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: BluetoothTestScreen(),
    );
  }
}

class BluetoothTestScreen extends StatefulWidget {
  @override
  _BluetoothTestScreenState createState() => _BluetoothTestScreenState();
}

class _BluetoothTestScreenState extends State<BluetoothTestScreen> {
  String _distance = "Connecting...";

  @override
  void initState() {
    super.initState();
    _connectToBluetooth();
  }

  void _connectToBluetooth() async {
    try {
      if (await FlutterBluetooth.isAvailable) {
        List<BluetoothDevice> devices = await FlutterBluetooth.scan();
        if (devices.isNotEmpty) {
          BluetoothDevice device = devices.first;
          await FlutterBluetooth.connect(device);
          FlutterBluetooth.onMessageReceived.listen((data) {
            setState(() {
              _distance = data; // Display received distance
            });
          });
        }
      } else {
        setState(() {
          _distance = "Bluetooth is not available";
        });
      }
    } catch (e) {
      setState(() {
        _distance = "Error: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Bluetooth Distance Test")),
      body: Center(
        child: Text(
          'Distance: $_distance cm',
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}

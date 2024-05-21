import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:image_picker/image_picker.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  File? _image;
  final picker = ImagePicker();

  Future getImageGallery() async {
    final PickedFile = await picker.pickImage(
      source: ImageSource.gallery,
      imageQuality: 80,
    );

    setState(() {
      if (PickedFile != null) {
        _image = File(PickedFile.path);
        //widget.imgUrl = null;
      } else {
        print("No Image Picked");
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: InkWell(
          onTap: () {
            getImageGallery();
          },
          child: Container(
              height: 200,
              width: 300,
              decoration: BoxDecoration(
                border: Border.all(color: Colors.grey),
              ),
              child: _image != null
                  ? Image.file(_image!.absolute, fit: BoxFit.cover)
                  : Center(
                      child: Icon(
                        Icons.add_photo_alternate_outlined,
                        size: 30,
                      ),
                    )),
        ),
      ),
    );
  }
}

package org.asr.tools;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import org.apache.sanselan.ImageReadException;
import org.apache.sanselan.Sanselan;
import org.apache.sanselan.common.IImageMetadata;
import org.apache.sanselan.common.RationalNumber;
import org.apache.sanselan.formats.jpeg.JpegImageMetadata;
import org.apache.sanselan.formats.tiff.TiffField;
import org.apache.sanselan.formats.tiff.TiffImageMetadata;
import org.apache.sanselan.formats.tiff.constants.TagInfo;
import org.apache.sanselan.formats.tiff.constants.TiffConstants;

public class Metadata {
	public static void main(String args[]) throws ImageReadException, IOException {
		// get all metadata stored in EXIF format (ie. from JPEG or TIFF).
		// org.w3c.dom.Node node = Sanselan.getMetadataObsolete(imageBytes);
		File file = new File("C:\\gichanga\\20180404_111908.jpg");
		IImageMetadata metadata = Sanselan.getMetadata(file);

		// System.out.println(metadata);
	
		if (metadata instanceof JpegImageMetadata) {
			JpegImageMetadata jpegMetadata = (JpegImageMetadata) metadata;

			// Jpeg EXIF metadata is stored in a TIFF-based directory structure
			// and is identified with TIFF tags.
			// Here we look for the "x resolution" tag, but
			// we could just as easily search for any other tag.
			//
			// see the TiffConstants file for a list of TIFF tags.
			/*
			System.out.println("file: " + file.getPath());

			// print out various interesting EXIF tags.
			printTagValue(jpegMetadata, TiffConstants.TIFF_TAG_XRESOLUTION);
			printTagValue(jpegMetadata, TiffConstants.TIFF_TAG_DATE_TIME);
			printTagValue(jpegMetadata, TiffConstants.EXIF_TAG_DATE_TIME_ORIGINAL);
			printTagValue(jpegMetadata, TiffConstants.EXIF_TAG_CREATE_DATE);
			printTagValue(jpegMetadata, TiffConstants.EXIF_TAG_ISO);
			printTagValue(jpegMetadata, TiffConstants.EXIF_TAG_SHUTTER_SPEED_VALUE);
			printTagValue(jpegMetadata, TiffConstants.EXIF_TAG_APERTURE_VALUE);
			printTagValue(jpegMetadata, TiffConstants.EXIF_TAG_BRIGHTNESS_VALUE);
			printTagValue(jpegMetadata, TiffConstants.GPS_TAG_GPS_LATITUDE_REF);
			printTagValue(jpegMetadata, TiffConstants.GPS_TAG_GPS_LATITUDE);
			printTagValue(jpegMetadata, TiffConstants.GPS_TAG_GPS_LONGITUDE_REF);
			printTagValue(jpegMetadata, TiffConstants.GPS_TAG_GPS_LONGITUDE);*/

			// simple interface to GPS data
			TiffImageMetadata exifMetadata = jpegMetadata.getExif();
			if (null != exifMetadata) {
				TiffImageMetadata.GPSInfo gpsInfo = exifMetadata.getGPS();
				if (null != gpsInfo) {
					String gpsDescription = gpsInfo.toString();
					double longitude = gpsInfo.getLongitudeAsDegreesEast();
					double latitude = gpsInfo.getLatitudeAsDegreesNorth();
					int altitude = Integer.valueOf(jpegMetadata.findEXIFValue(TiffConstants.GPS_TAG_GPS_ALTITUDE).getValueDescription().replaceAll(",", ""));

					System.out.println("1," + latitude + " " + longitude + " " + altitude + "," +
							jpegMetadata.findEXIFValue(TiffConstants.EXIF_TAG_DATE_TIME_ORIGINAL).getValueDescription());
				}
			}
		}
	}

	private static void printTagValue(JpegImageMetadata jpegMetadata, TagInfo tagInfo)
			throws ImageReadException, IOException {
		TiffField field = jpegMetadata.findEXIFValue(tagInfo);
		if (field == null)
			System.out.println(tagInfo.name + ": " + "Not Found.");
		else
			System.out.println(tagInfo.name + ": " + field.getValueDescription());
	}

}

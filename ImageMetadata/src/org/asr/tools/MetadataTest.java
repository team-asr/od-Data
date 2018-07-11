/**
 * 
 */
package org.asr.tools;

import static org.junit.jupiter.api.Assertions.fail;

import java.io.IOException;

import org.apache.sanselan.ImageReadException;
import org.junit.jupiter.api.Test;

/**
 * @author gichangA
 *
 */
public class MetadataTest {
	static private final String filename = "C:\\gichanga\\ASR\\Consultancy & Funding\\UAS-Imagery\\od-Data\\raw-images\\IMG_170504_081552_0002_RGB.JPG";

	/**
	 * Test method for {@link org.asr.tools.Metadata#main(java.lang.String[])}.
	 */
	@Test
	public void testMain() {
		try {
			Metadata.main(new String[] {filename});
		} catch (ImageReadException | IOException e) {
			fail(e.getMessage());
		}
	}

	/**
	 * Test method for {@link org.asr.tools.Metadata#Metadata()}.
	 */
	@Test
	public void testMetadata() {
	}

	/**
	 * Test method for {@link org.asr.tools.Metadata#Metadata(java.lang.String)}.
	 */
	@Test
	public void testMetadataString() {
		try {
			Metadata meta = new Metadata(filename);
		} catch (ImageReadException | IOException e) {
			fail(e.getMessage());
		}

	}

	/**
	 * Test method for {@link org.asr.tools.Metadata#usage()}.
	 */
	@Test
	public void testUsage() {
		Metadata meta = new Metadata();
		meta.usage();
	}

}

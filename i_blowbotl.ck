// To run: 
// chuck scale instrument:volume:speed:octave:shift:scale:instrument
// chuck scale.ck melody.ck:50:2:5:1:0
// 
// http://chuck.cs.princeton.edu/doc/program/ugen.html
// Instruments: BandedWG BlowBotl BlowHole Bowed Brass Clarinet Mandolin ModalBar Moog Saxofony Shakers Sitar StifKarp

// initialize Scale
Scale sc;

// initialize instrument 
BlowBotl inst => dac; 

// get arguments from command line
int volume; 
int speed; 
int octave; 
int shift; 
int scale; // 0 - maj, 1 - nat min, 2 - har min 
if( me.args() ) 
{
	me.arg(0) => Std.atoi => volume;
	if( volume > 80 )
	{
		80 => volume; 
	}
	if( volume < 1 )
	{
		1 => volume; 
	}
	
	me.arg(1) => Std.atoi => speed; 
	if( speed > 10 )
	{
		10 => speed; 
	}
	if( speed < 1 )
	{
		1 => speed; 
	}
	
	me.arg(2) => Std.atoi => octave;
	if( octave > 10 )
	{
		10 => octave; 
	}
	if( octave < 0 )
	{
		0 => octave; 
	}
	
	me.arg(3) => Std.atoi => shift;
	if( shift > 12 )
	{
		12 => shift; 
	}
	if( shift < 0 )
	{
		0 => shift; 
	}
	
	me.arg(4) => Std.atoi => scale;
	if( scale > 2 )
	{
		2 => scale; 
	}
	if( scale < 0 )
	{
		0 => scale; 
	}
}

//-Functions-// 

fun int play()
{
	if( scale == 0 )
	{
		play2(sc.maj); 
	}
	if( scale == 1 )
	{
		play2(sc.min); 
	}
	if( scale == 2 )
	{
		play2(sc.har); 
	} 	
	return 0; 
}

fun int play2(int scale[]) 
{
    for (0=>int i; true; i++) //infinite loop
	{
		Std.mtof( octave * 12 + shift + sc.scale( Math.random2(0,7), scale )) => inst.freq; //set the note with intended octave, shift, and scale 
		inst.noteOn( volume / 100. ); //play a note at intended volume 
		(1000/speed)::ms => now; //compute audio at intended speed 
	}
    return 0;
}

//------------//

// play 
play(); 

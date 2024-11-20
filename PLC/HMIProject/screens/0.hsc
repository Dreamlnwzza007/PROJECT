<?xml version="1.0" encoding="utf-8"?>
<ScrInfo ScreenNo="0" ScreenType="" ScreenSize="0">
	<PartInfo PartType="Text" PartName="TXT_0" PartClassifyType="OtherClassType" PartID="0_TXT_0">
		<General TextContent="SETPOINT TANK2" LaFrnColor="0x0 0" IsBackColor="0" BgColor="0xfdf0c4 0" CharSize="1414141414141414" Bold="0" StartPt="85 39" Width="0" Height="0" Area="85 39 267 65" InAlign="1" Locking="0" IsEnableStringTable="0" GroupNames="ID:-01" IsDynamic="0" StaticTextId="-1" />
	</PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_1" PartClassifyType="InputAndShow" PartID="0_NUM_1">
		<General Desc="NUM_1" Area="112 79 236 133" CharSize="1414141414141414" WordAddr="MW0" Fast="0" HighLowChange="0" IsInput="1" WriteAddr="MW0" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" IsKeyBoardRemark="0" LaStartPt="0 0" BorderColor="0xf7e7ad 0" LaFrnColor="0x0 0" BgColor="0xfdf0c4 0" BmpIndex="102" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" KbdContinue="0" KbdContinueNum="0" KbdContinueGroup="0" KbdContinueEnd="0" IsShowNaturalDecimals="0" Locking="0" />
		<SVGColor svgfile="Rectangle\Rectangle0105.svg" dark="0x0 0" light="0xffffff 0" hlight="0x0 0" shadow="0xc0c0c0 0" shape="0x0 0" gstartcolor="0x0 0" gmidcolor="0x0 0" gendcolor="0x0 0" />
		<DispFormat DispType="105" DigitCount="2 0" DataLimit="0105 02 00 0 40" IsVar="0" Zoom="0" Mutiple="1.000000000000000" Round="0" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0" UseOutRangeText="0" />
		<MoveZoom DataFormatMZ="0" MutipleMZ="1.000000000000000" />
		<TrigHide UseShowHide="0" HideType="0" IsHideAllTime="0" />
		<Extension TouchState="1" Buzzer="1" IsCheck="0" AckTime="20" CtrlType="0" DataFormat="105" />
		<Lock Lockmate="0" UnDrawLock="0" LockMode="0" IsShowGrayScale="0" />
		<PartPwd IsUesPartPassword="0" IsSetLowerLev="0" PartPasswordLev="0" />
		<ClickPopTrig />
		<UserAuthority IsUseUserAuthority="0" IsPopUserLoginWin="0" PopType="0" IsHidePart="0" />
	</PartInfo>
	<PartInfo PartType="GroupPart" PartName="Group Objects">
		<PartInfo PartType="Numeric" PartName="NUM_0" PartClassifyType="InputAndShow" PartID="0_NUM_0">
			<General Desc="NUM_0" Area="31 170 143 286" CharSize="1414141414141414" Fast="0" HighLowChange="0" IsInput="0" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" IsKeyBoardRemark="0" LaStartPt="0 0" BorderColor="0xf7e7ad 0" LaFrnColor="0x0 0" BgColor="0xfdf0c4 0" BmpIndex="101" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" KbdContinue="0" KbdContinueNum="0" KbdContinueGroup="0" KbdContinueEnd="0" IsShowNaturalDecimals="0" Locking="0" />
			<SVGColor svgfile="Tanks\Tanks1089.svg" dark="0x0 0" light="0x0 0" hlight="0x0 0" shadow="0x0 0" shape="0x0 0" gstartcolor="0x0 0" gmidcolor="0x0 0" gendcolor="0x0 0" />
			<DispFormat DispType="105" DigitCount="5 0" DataLimit="0105 05 00 0 65535" IsVar="0" Zoom="0" Mutiple="1.000000000000000" Round="0" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0" UseOutRangeText="0" />
			<MoveZoom DataFormatMZ="0" MutipleMZ="1.000000000000000" />
			<TrigHide UseShowHide="0" HideType="0" IsHideAllTime="0" />
			<Extension TouchState="1" Buzzer="1" IsCheck="0" AckTime="20" CtrlType="0" DataFormat="105" />
			<Lock Lockmate="0" UnDrawLock="0" LockMode="0" IsShowGrayScale="0" />
			<PartPwd IsUesPartPassword="0" IsSetLowerLev="0" PartPasswordLev="0" />
			<ClickPopTrig />
			<UserAuthority IsUseUserAuthority="0" IsPopUserLoginWin="0" PopType="0" IsHidePart="0" />
		</PartInfo>
		<PartInfo PartType="Bar" PartName="BAR_0" PartClassifyType="Instrument" PartID="0_BAR_0">
			<General Desc="BAR_0" Area="31 177 149 282" WordAddr="MW18" IsMarkVar="0" MarkRange="0105 05 00 0 40" BarType="0" MeTxtColor="0x40 0" ShowMeBg="1" MeBgColor="0xc0c0c0 0" ShowScale="1" Scale="4" LongIntval="0" ScaleColor="0x0 0" LongIntvalColor="0x0 0" AreaCount="1" BUseDValue="0" IsWaringAddr="0" IsShowNum="0" Locking="0" />
			<AlarmArea Status="0" AlarmValue="40" AlarmValue2="0" MeAlColor="0xff0000 0" />
			<AlarmArea Status="1" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="2" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="3" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
		</PartInfo>
	</PartInfo>
	<PartInfo PartType="GroupPart" PartName="Group Objects">
		<PartInfo PartType="Numeric" PartName="NUM_2" PartClassifyType="InputAndShow" PartID="0_NUM_2">
			<General Desc="NUM_0" Area="199 170 311 286" CharSize="1414141414141414" Fast="0" HighLowChange="0" IsInput="0" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" IsKeyBoardRemark="0" LaStartPt="0 0" BorderColor="0xf7e7ad 0" LaFrnColor="0x0 0" BgColor="0xfdf0c4 0" BmpIndex="101" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" KbdContinue="0" KbdContinueNum="0" KbdContinueGroup="0" KbdContinueEnd="0" IsShowNaturalDecimals="0" Locking="0" />
			<SVGColor svgfile="Tanks\Tanks1089.svg" dark="0x0 0" light="0x0 0" hlight="0x0 0" shadow="0x0 0" shape="0x0 0" gstartcolor="0x0 0" gmidcolor="0x0 0" gendcolor="0x0 0" />
			<DispFormat DispType="105" DigitCount="5 0" DataLimit="0105 05 00 0 65535" IsVar="0" Zoom="0" Mutiple="1.000000000000000" Round="0" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0" UseOutRangeText="0" />
			<MoveZoom DataFormatMZ="0" MutipleMZ="1.000000000000000" />
			<TrigHide UseShowHide="0" HideType="0" IsHideAllTime="0" />
			<Extension TouchState="1" Buzzer="1" IsCheck="0" AckTime="20" CtrlType="0" DataFormat="105" />
			<Lock Lockmate="0" UnDrawLock="0" LockMode="0" IsShowGrayScale="0" />
			<PartPwd IsUesPartPassword="0" IsSetLowerLev="0" PartPasswordLev="0" />
			<ClickPopTrig />
			<UserAuthority IsUseUserAuthority="0" IsPopUserLoginWin="0" PopType="0" IsHidePart="0" />
		</PartInfo>
		<PartInfo PartType="Bar" PartName="BAR_1" PartClassifyType="Instrument" PartID="0_BAR_1">
			<General Desc="BAR_0" Area="199 177 317 282" WordAddr="MW18" IsMarkVar="0" MarkRange="0105 05 00 0 40" BarType="0" MeTxtColor="0x0 0" ShowMeBg="1" MeBgColor="0xc0c0c0 0" ShowScale="1" Scale="4" LongIntval="0" ScaleColor="0x0 0" LongIntvalColor="0x0 0" AreaCount="1" BUseDValue="0" IsWaringAddr="0" IsShowNum="0" Locking="0" />
			<AlarmArea Status="0" AlarmValue="40" AlarmValue2="0" MeAlColor="0xff0000 0" />
			<AlarmArea Status="1" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="2" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="3" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
		</PartInfo>
	</PartInfo>
	<PartInfo PartType="GroupPart" PartName="Group Objects">
		<PartInfo PartType="Numeric" PartName="NUM_3" PartClassifyType="InputAndShow" PartID="0_NUM_3">
			<General Desc="NUM_0" Area="31 304 143 420" CharSize="1414141414141414" Fast="0" HighLowChange="0" IsInput="0" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" IsKeyBoardRemark="0" LaStartPt="0 0" BorderColor="0xf7e7ad 0" LaFrnColor="0x0 0" BgColor="0xfdf0c4 0" BmpIndex="101" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" KbdContinue="0" KbdContinueNum="0" KbdContinueGroup="0" KbdContinueEnd="0" IsShowNaturalDecimals="0" Locking="0" />
			<SVGColor svgfile="Tanks\Tanks1089.svg" dark="0x0 0" light="0x0 0" hlight="0x0 0" shadow="0x0 0" shape="0x0 0" gstartcolor="0x0 0" gmidcolor="0x0 0" gendcolor="0x0 0" />
			<DispFormat DispType="105" DigitCount="5 0" DataLimit="0105 05 00 0 65535" IsVar="0" Zoom="0" Mutiple="1.000000000000000" Round="0" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0" UseOutRangeText="0" />
			<MoveZoom DataFormatMZ="0" MutipleMZ="1.000000000000000" />
			<TrigHide UseShowHide="0" HideType="0" IsHideAllTime="0" />
			<Extension TouchState="1" Buzzer="1" IsCheck="0" AckTime="20" CtrlType="0" DataFormat="105" />
			<Lock Lockmate="0" UnDrawLock="0" LockMode="0" IsShowGrayScale="0" />
			<PartPwd IsUesPartPassword="0" IsSetLowerLev="0" PartPasswordLev="0" />
			<ClickPopTrig />
			<UserAuthority IsUseUserAuthority="0" IsPopUserLoginWin="0" PopType="0" IsHidePart="0" />
		</PartInfo>
		<PartInfo PartType="Bar" PartName="BAR_2" PartClassifyType="Instrument" PartID="0_BAR_2">
			<General Desc="BAR_0" Area="31 311 149 416" WordAddr="MW12" IsMarkVar="0" MarkRange="0105 05 00 0 40" BarType="0" MeTxtColor="0x0 0" ShowMeBg="1" MeBgColor="0xc0c0c0 0" ShowScale="1" Scale="4" LongIntval="0" ScaleColor="0x0 0" LongIntvalColor="0x0 0" AreaCount="1" BUseDValue="0" IsWaringAddr="0" IsShowNum="0" Locking="0" />
			<AlarmArea Status="0" AlarmValue="40" AlarmValue2="0" MeAlColor="0xff0000 0" />
			<AlarmArea Status="1" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="2" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="3" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
		</PartInfo>
	</PartInfo>
	<PartInfo PartType="GroupPart" PartName="Group Objects">
		<PartInfo PartType="Numeric" PartName="NUM_4" PartClassifyType="InputAndShow" PartID="0_NUM_4">
			<General Desc="NUM_0" Area="199 304 311 420" CharSize="1414141414141414" Fast="0" HighLowChange="0" IsInput="0" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" IsKeyBoardRemark="0" LaStartPt="0 0" BorderColor="0xf7e7ad 0" LaFrnColor="0x0 0" BgColor="0xfdf0c4 0" BmpIndex="101" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" KbdContinue="0" KbdContinueNum="0" KbdContinueGroup="0" KbdContinueEnd="0" IsShowNaturalDecimals="0" Locking="0" />
			<SVGColor svgfile="Tanks\Tanks1089.svg" dark="0x0 0" light="0x0 0" hlight="0x0 0" shadow="0x0 0" shape="0x0 0" gstartcolor="0x0 0" gmidcolor="0x0 0" gendcolor="0x0 0" />
			<DispFormat DispType="105" DigitCount="5 0" DataLimit="0105 05 00 0 65535" IsVar="0" Zoom="0" Mutiple="1.000000000000000" Round="0" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0" UseOutRangeText="0" />
			<MoveZoom DataFormatMZ="0" MutipleMZ="1.000000000000000" />
			<TrigHide UseShowHide="0" HideType="0" IsHideAllTime="0" />
			<Extension TouchState="1" Buzzer="1" IsCheck="0" AckTime="20" CtrlType="0" DataFormat="105" />
			<Lock Lockmate="0" UnDrawLock="0" LockMode="0" IsShowGrayScale="0" />
			<PartPwd IsUesPartPassword="0" IsSetLowerLev="0" PartPasswordLev="0" />
			<ClickPopTrig />
			<UserAuthority IsUseUserAuthority="0" IsPopUserLoginWin="0" PopType="0" IsHidePart="0" />
		</PartInfo>
		<PartInfo PartType="Bar" PartName="BAR_3" PartClassifyType="Instrument" PartID="0_BAR_3">
			<General Desc="BAR_0" Area="199 311 317 416" WordAddr="MW12" IsMarkVar="0" MarkRange="0105 05 00 0 40" BarType="0" MeTxtColor="0x0 0" ShowMeBg="1" MeBgColor="0xc0c0c0 0" ShowScale="1" Scale="4" LongIntval="0" ScaleColor="0x0 0" LongIntvalColor="0x0 0" AreaCount="1" BUseDValue="0" IsWaringAddr="0" IsShowNum="0" Locking="0" />
			<AlarmArea Status="0" AlarmValue="40" AlarmValue2="0" MeAlColor="0xff0000 0" />
			<AlarmArea Status="1" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="2" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
			<AlarmArea Status="3" AlarmValue="0" AlarmValue2="0" MeAlColor="0x0 0" />
		</PartInfo>
	</PartInfo>
	<PartInfo PartType="HisTrend" PartName="HIS_0" PartClassifyType="TableAndCurve" PartID="0_HIS_0">
		<General Desc="HIS_0" Area="328 21 792 248" IsVar="0" CharSize="1414141414141414" DataLimit="0204 10 00 0 40" StartTime="0 0 0" XScale="5" YScale="5" UseDynamicCurve="0" BgColor="0xffffff 0" BgType="4" GridColor="0x0 0" BgColor1="0x62c89e 0" BgColor2="0xffffff 0" ScaleValueColor="0x0 0" ScaleColor="0x0 0" TranValue="100" UseSlider="0" TranSlide="100" ShowPt="0" SliderColor="0x0 0" bUseFont="0" UseDataFormat="0" Table_TimeFormat="262144" Table_TimeType="1" LogID="1" IsIdVar="0" OpenModeStartAddr="HDW0" TimeSpan="1/2" ScreenNo="4002" SampleShowCurve="0" Locking="0" />
		<Channel Status="0" Use="1" SubID="3" LineColor="0xff0000 0" LineWidth="3" LineType="1" SampleEnable="0" SampleLineWidth="0" SampleLineColor="0x0 0" SampleCustomYEnable="0" SampleYOnRight="0" />
		<Channel Status="1" Use="1" SubID="2" LineColor="0x4080ff 0" LineWidth="3" LineType="1" SampleEnable="0" SampleLineWidth="0" SampleLineColor="0x0 0" SampleCustomYEnable="0" SampleYOnRight="0" />
		<Channel Status="2" Use="1" SubID="1" LineColor="0xff00 0" LineWidth="3" LineType="1" SampleEnable="0" SampleLineWidth="0" SampleLineColor="0x0 0" SampleCustomYEnable="0" SampleYOnRight="0" />
	</PartInfo>
	<PartInfo PartType="HisTrend" PartName="HIS_1" PartClassifyType="TableAndCurve" PartID="0_HIS_1">
		<General Desc="HIS_0" Area="328 230 792 457" IsVar="0" CharSize="1414141414141414" DataLimit="0204 10 00 0 100" StartTime="0 0 0" XScale="5" YScale="5" UseDynamicCurve="0" BgColor="0xffffff 0" BgType="4" GridColor="0x0 0" BgColor1="0x62c89e 0" BgColor2="0xffffff 0" ScaleValueColor="0x0 0" ScaleColor="0x0 0" TranValue="100" UseSlider="0" TranSlide="100" ShowPt="0" SliderColor="0x0 0" bUseFont="0" UseDataFormat="0" Table_TimeFormat="262144" Table_TimeType="1" LogID="2" IsIdVar="0" OpenModeStartAddr="HDW0" TimeSpan="1/2" ScreenNo="4002" SampleShowCurve="0" Locking="0" />
		<Channel Status="0" Use="1" SubID="1" LineColor="0xff 0" LineWidth="3" LineType="1" SampleEnable="0" SampleLineWidth="0" SampleLineColor="0x0 0" SampleCustomYEnable="0" SampleYOnRight="0" />
		<Channel Status="1" Use="1" SubID="2" LineColor="0x800080 0" LineWidth="3" LineType="1" SampleEnable="0" SampleLineWidth="0" SampleLineColor="0x0 0" SampleCustomYEnable="0" SampleYOnRight="0" />
	</PartInfo>
</ScrInfo>

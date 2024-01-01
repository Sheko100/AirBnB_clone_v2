<!DOCTYPE html>
<HTML lang="en">
	<HEAD>
		<TITLE>HBNB</TITLE>
	</HEAD>
	<BODY>
		<H1>States</H1>
		<UL>
		{% for state in states|sort %}
			<LI>
				{{ state.id }}: <B>{{ state.name }}</B>
				<UL>
					<LI>{{ state.city.id }}: <B>state.city.name</B></LI>
				</UL>
			</LI>
		{% endfor %}
		</UL>
	</BODY>
</HTML>

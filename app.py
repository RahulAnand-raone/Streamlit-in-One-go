import streamlit as st
st.title('Title -> Hello World')                #Title
st.header('Header -> Geek for Geeks')           #header
st.subheader('Subheader -> GFG')                #Subheader
st.text('Text -> Text')                         # text

st.markdown('# Hi')                             # markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

st.success('Success!')                          #success
st.info('Information!')                         #Info
st.warning('Warning')                           ## WARNING
st.error('Error!')                              #Error
st.exception(ZeroDivisionError('Division not possible with 0')) #exception

st.help(ZeroDivisionError)                      #help

st.write("range(1,10)")                         #write
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x=10 \n'                               #code
        'for i in range(x): \n'
        '\tprint(i)')


st.checkbox('Male')                             #Checkbox
st.checkbox('Female')

if(st.checkbox('Adult')):                       #Checkbox with Validation
    st.write('You are an Adult!')

st.subheader('Radio Button')                    #radioButton
radioButton = st.radio('Select: ', ('Male', 'Female', 'Other'))

if(radioButton=='Male'):
    st.write('You are Male')
elif(radioButton=='Female'):
    st.write('You are Female')
elif(radioButton=='Other'):
    st.write('You are Other')

st.subheader('Select Box')                          #SelectBox
SelectBox = st.selectbox("Data Science: ", ['Data Analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning',
                                'NLP', 'Computer Vision', 'Image Processing'])
st.write("You've selected : ", SelectBox)

st.subheader('MultiSelect Box')                     #MultiSelectBox
MultiSelBox = st.multiselect("Data Science: ", ['Data Analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning',
                                'NLP', 'Computer Vision', 'Image Processing'])
st.write("You've selected : ", len(MultiSelBox), 'courses')

st.subheader('Button')
st.button('Click Me!')                                 #Button

st.subheader('Slider')                                  #Slider
vol = st.slider('Select the Volume: ',1,100,step=1)
st.write('The volume is: ',vol)

st.subheader('Text Input')                              #Text-Input
username = st.text_input('Username: ')
password = st.text_input('Password: ', type='password')
st.write('Hi!', username)


st.subheader('Text Area')
textArea = st.text_area('Write about yourself in 500 words')     #Text-Area
st.write(textArea)

st.subheader('Input Number: ')                                     ##Text-Number
st.number_input("Select your age: ",18,100)

st.subheader('Input Date: ')
st.date_input('Date')                                              #Text-Date

st.subheader('Input Time: ')                                        # Text-Time
st.time_input('Time')

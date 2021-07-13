% import two different images
image1 = imread('Plane','jpg')
image2 = imread('Nature','jpg')

% show the images
figure, imshow(image1)
title('The image of the Plane')

figure, imshow(image2)
title('The image of the Nature')

% applying 2-Dimentional FFT processes
fourier1 = fft2(double(image1))
fourier2 = fft2(double(image2))

% show the magnitude and phase of two images on frequency domain.
figure, imshow(abs(fftshift(fourier1)),[24 100000]), colormap gray
title('The image of the Plane - Magnitude')

figure, imshow(angle(fftshift(fourier1)),[-pi pi]), colormap gray
title('The image of the Nature - Phase Angle')

figure, imshow(abs(fftshift(fourier2)),[24 100000]), colormap gray
title('The image of the Nature - Magnitude')

figure, imshow(angle(fftshift(fourier2)),[-pi pi]), colormap gray
title('The image of the Nature - Phase Angle')

% switch magnitude and phase angle of these images.
fourier3 = abs(fourier1).*exp(i*angle(fourier2))
fourier4 = abs(fourier2).*exp(i*angle(fourier1))

% applying inverse-FFT to the fourier3 and fourier4.
imageResult1 = ifft2(fourier3)
imageResult2 = ifft2(fourier4)

% To display these switched images
% interval values(min and max) of the image 
min1 = min(min(abs(imageResult1)))
max1 = max(max(abs(imageResult1)))
figure, imshow(abs(imageResult1), [min1 max1]), colormap gray
title('Image Result 1')

min2 = min(min(abs(imageResult2)))
max2 = max(max(abs(imageResult2)))
figure, imshow(abs(imageResult2), [min2 max2]), colormap gray
title('Image Result 2')

% To save results
%{
saveas(1, 'imageResult1.png')
saveas(2, 'imageResult2.png')
%}